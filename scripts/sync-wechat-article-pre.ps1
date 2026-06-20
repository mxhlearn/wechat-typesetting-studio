param(
    [switch]$Check,
    [switch]$Apply,
    [switch]$Watch,
    [string]$WorkspaceSkill = "",
    [string]$InstalledSkill = "",
    [int]$IntervalSeconds = 3
)

$ErrorActionPreference = "Stop"

function Resolve-FullPath {
    param([string]$Path)
    $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Path)
}

function Get-DefaultWorkspaceSkill {
    $repoRoot = Resolve-FullPath (Join-Path $PSScriptRoot "..")
    Join-Path $repoRoot "skills\wechat-article-pre"
}

function Get-DefaultInstalledSkill {
    Join-Path $env:USERPROFILE ".codex\skills\wechat-article-pre"
}

function Assert-SkillPath {
    param(
        [string]$Path,
        [string]$Kind
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "$Kind path does not exist: $Path"
    }

    $skillFile = Join-Path $Path "SKILL.md"
    if (-not (Test-Path -LiteralPath $skillFile)) {
        throw "$Kind path is not a skill folder: $Path"
    }
}

function Assert-InstallTargetSafe {
    param([string]$Path)

    $full = Resolve-FullPath $Path
    $expectedSuffix = ".codex\skills\wechat-article-pre"

    if (-not $full.EndsWith($expectedSuffix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to write outside the expected installed skill path: $full"
    }

    if ((Split-Path -Leaf $full) -ne "wechat-article-pre") {
        throw "Refusing to write a target whose folder name is not wechat-article-pre: $full"
    }

    return $full
}

function Get-FileMap {
    param([string]$Root)

    $map = @{}
    Get-ChildItem -LiteralPath $Root -Recurse -File | ForEach-Object {
        $relative = $_.FullName.Substring($Root.Length).TrimStart("\")
        $map[$relative] = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
    }
    return $map
}

function Compare-SkillFolders {
    param(
        [string]$Source,
        [string]$Target
    )

    Assert-SkillPath -Path $Source -Kind "Workspace"

    if (-not (Test-Path -LiteralPath $Target)) {
        return @([pscustomobject]@{ Path = "."; Status = "InstalledMissing" })
    }

    Assert-SkillPath -Path $Target -Kind "Installed"

    $sourceMap = Get-FileMap -Root $Source
    $targetMap = Get-FileMap -Root $Target
    $allPaths = @($sourceMap.Keys + $targetMap.Keys) | Sort-Object -Unique

    $diff = foreach ($path in $allPaths) {
        $sourceHash = $sourceMap[$path]
        $targetHash = $targetMap[$path]
        if ($sourceHash -ne $targetHash) {
            $status = if ($null -eq $sourceHash) {
                "OnlyInstalled"
            } elseif ($null -eq $targetHash) {
                "OnlyWorkspace"
            } else {
                "Different"
            }
            [pscustomobject]@{ Path = $path; Status = $status }
        }
    }

    return @($diff)
}

function Sync-Skill {
    param(
        [string]$Source,
        [string]$Target
    )

    Assert-SkillPath -Path $Source -Kind "Workspace"
    $safeTarget = Assert-InstallTargetSafe -Path $Target
    $targetParent = Split-Path -Parent $safeTarget

    if (-not (Test-Path -LiteralPath $targetParent)) {
        New-Item -ItemType Directory -Force -Path $targetParent | Out-Null
    }

    if (-not (Test-Path -LiteralPath $safeTarget)) {
        New-Item -ItemType Directory -Force -Path $safeTarget | Out-Null
    }

    Get-ChildItem -LiteralPath $Source -Recurse -Directory | ForEach-Object {
        $relative = $_.FullName.Substring($Source.Length).TrimStart("\")
        $targetDir = Join-Path $safeTarget $relative
        if (-not (Test-Path -LiteralPath $targetDir)) {
            New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
        }
    }

    $sourceMap = Get-FileMap -Root $Source
    foreach ($relative in $sourceMap.Keys) {
        $sourceFile = Join-Path $Source $relative
        $targetFile = Join-Path $safeTarget $relative
        $targetDir = Split-Path -Parent $targetFile
        if (-not (Test-Path -LiteralPath $targetDir)) {
            New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
        }
        Copy-Item -LiteralPath $sourceFile -Destination $targetFile -Force
    }

    if (Test-Path -LiteralPath $safeTarget) {
        Get-ChildItem -LiteralPath $safeTarget -Recurse -File | ForEach-Object {
            $relative = $_.FullName.Substring($safeTarget.Length).TrimStart("\")
            if (-not $sourceMap.ContainsKey($relative)) {
                Remove-Item -LiteralPath $_.FullName -Force
            }
        }

        Get-ChildItem -LiteralPath $safeTarget -Recurse -Directory |
            Sort-Object FullName -Descending |
            ForEach-Object {
                if (-not (Get-ChildItem -LiteralPath $_.FullName -Force)) {
                    Remove-Item -LiteralPath $_.FullName -Force
                }
            }
    }
}

function Show-CheckResult {
    param(
        [object[]]$Diff
    )

    if ($Diff.Count -eq 0) {
        Write-Output "MATCH: workspace and installed skill are identical."
        return
    }

    Write-Output "DIFFER: workspace and installed skill are not identical."
    $Diff | Sort-Object Path | Format-Table -AutoSize
}

if (-not $WorkspaceSkill) {
    $WorkspaceSkill = Get-DefaultWorkspaceSkill
}

if (-not $InstalledSkill) {
    $InstalledSkill = Get-DefaultInstalledSkill
}

$WorkspaceSkill = Resolve-FullPath $WorkspaceSkill
$InstalledSkill = if (Test-Path -LiteralPath $InstalledSkill) {
    Resolve-FullPath $InstalledSkill
} else {
    $InstalledSkill
}

if (-not $Check -and -not $Apply -and -not $Watch) {
    $Check = $true
}

if ($Watch) {
    Write-Output "Watching workspace skill and keeping installed skill in sync."
    Write-Output "Workspace: $WorkspaceSkill"
    Write-Output "Installed: $InstalledSkill"
    while ($true) {
        $diff = Compare-SkillFolders -Source $WorkspaceSkill -Target $InstalledSkill
        Show-CheckResult -Diff $diff
        if ($diff.Count -ne 0) {
            if ($Apply) {
                Sync-Skill -Source $WorkspaceSkill -Target $InstalledSkill
                $diff = Compare-SkillFolders -Source $WorkspaceSkill -Target $InstalledSkill
                Show-CheckResult -Diff $diff
            } else {
                Write-Output "Run again with -Apply to sync."
            }
        }
        Start-Sleep -Seconds $IntervalSeconds
    }
}

if ($Apply) {
    Sync-Skill -Source $WorkspaceSkill -Target $InstalledSkill
}

$diff = Compare-SkillFolders -Source $WorkspaceSkill -Target $InstalledSkill
Show-CheckResult -Diff $diff

if ($diff.Count -eq 0) {
    exit 0
}

exit 2
