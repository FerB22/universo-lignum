Add-Type -AssemblyName System.Web

$chapters = @(
    @{ num=1;  slug="capitulo_01"; title="El peso de los tatuajes";           md="Capitulo_01_El_peso_de_los_tatuajes.md" },
    @{ num=2;  slug="capitulo_02"; title="El consejo de Hiltar";              md="Capitulo_02_El_consejo_de_Hiltar.md" },
    @{ num=3;  slug="capitulo_03"; title="Tierra sagrada";                    md="Capitulo_03_Tierra_sagrada.md" },
    @{ num=4;  slug="capitulo_04"; title="Entrenamiento y temores";           md="Capitulo_04_Entrenamiento_y_temores.md" },
    @{ num=5;  slug="capitulo_05"; title="El Conclave tribal";                md="Capitulo_05_El_conclave_tribal.md" },
    @{ num=6;  slug="capitulo_06"; title="Bajo la lluvia embarrada";          md="Capitulo_06_Bajo_la_lluvia_embarrada.md" },
    @{ num=7;  slug="capitulo_07"; title="La responsabilidad del lider";      md="Capitulo_07_La_responsabilidad_del_lider.md" },
    @{ num=8;  slug="capitulo_08"; title="El nacimiento en tiempos de guerra";md="Capitulo_08_El_nacimiento_en_tiempos_de_guerra.md" },
    @{ num=9;  slug="capitulo_09"; title="La necesidad de la guerra";         md="Capitulo_09_La_necesidad_de_la_guerra.md" },
    @{ num=10; slug="capitulo_10"; title="El perdon y el vacio";              md="Capitulo_10_El_perdon_y_el_vacio.md" },
    @{ num=11; slug="capitulo_11"; title="Miedo al conflicto";                md="Capitulo_11_Miedo_al_conflicto.md" },
    @{ num=12; slug="capitulo_12"; title="La caida de las murallas";          md="Capitulo_12_La_caida_de_las_murallas.md" },
    @{ num=13; slug="capitulo_13"; title="El retorno de la caballeria";       md="Capitulo_13_El_retorno_de la_caballeria.md" },
    @{ num=14; slug="capitulo_14"; title="El renacer de la paz";             md="Capitulo_14_El_renacer_de_la_paz.md"; inProgress=$true }
)

$displayTitles = @(
    "El peso de los tatuajes",
    "El consejo de H&iacute;ltar",
    "Tierra sagrada",
    "Entrenamiento y temores",
    "El C&oacute;nclave tribal",
    "Bajo la lluvia embarrada",
    "La responsabilidad del l&iacute;der",
    "El nacimiento en tiempos de guerra",
    "La necesidad de la guerra",
    "El perd&oacute;n y el vac&iacute;o",
    "Miedo al conflicto",
    "La ca&iacute;da de las murallas",
    "El retorno de la caballer&iacute;a",
    "El renacer de la paz (En proceso)"
)

$mdBase  = "C:\Users\Barra\Documents\Forgotten Sword - Historia Completa\Forgotten_Sword_Editado"
$outBase = "C:\Users\Barra\Documents\Forgotten Sword - Historia Completa\Fichas_Personajes\capitulos"
$tplPath = "C:\Users\Barra\Documents\Forgotten Sword - Historia Completa\Fichas_Personajes\chapter_template.html"

if (!(Test-Path $outBase)) { New-Item -ItemType Directory -Path $outBase | Out-Null }

# ---- Sidebar HTML ----
function Build-Sidebar([int]$currentNum) {
    $sb = [System.Text.StringBuilder]::new()
    [void]$sb.Append('<ul class="sidebar-list">')
    [void]$sb.Append('<li><a href="../prologo.html">Prologo</a></li>')
    foreach ($ch in $chapters) {
        $active = if ($ch.num -eq $currentNum) { ' class="active"' } else { '' }
        $disp = $displayTitles[$ch.num - 1]
        if ($ch.inProgress) {
            [void]$sb.Append("<li style=`"opacity:0.6; cursor:default;`"><a href=`"javascript:void(0)`" style=`"cursor:default; pointer-events:none; color:#a89274;`"><span class=`"ch-num`">$('{0:00}' -f $ch.num)</span> $disp</a></li>")
        } else {
            [void]$sb.Append("<li$active><a href=`"$($ch.slug).html`"><span class=`"ch-num`">$('{0:00}' -f $ch.num)</span> $disp</a></li>")
        }
    }
    [void]$sb.Append('</ul>')
    return $sb.ToString()
}

# ---- MD Body to HTML ----
function Convert-MDBody([string]$raw) {
    # 1. Remove YAML front matter
    $body = $raw -replace '(?s)^---.*?---\s*', ''
    # 2. Remove H1 header
    $body = $body -replace '(?m)^# .+', ''
    # 3. Strip any trailing navigation block at the end of the file
    $body = $body -replace '(?s)\s*---\s*[\r\n\s]*.*?(Capitulo_\d+|Forgotten%20Sword).*$', ''

    $lines = $body -split '\r?\n'
    $html = [System.Text.StringBuilder]::new()

    foreach ($line in $lines) {
        $t = $line.Trim()

        # Skip any line containing Markdown links to chapters or index
        if ($t -match 'Capitulo_\d+' -or $t -match 'Cap&iacute;tulo' -or $t -match '\[.*?(Capítulo|Capitulo|Índice|Indice).*?\]' -or $t -match 'Forgotten%20Sword') {
            continue
        }

        # Epigraph blockquote (starts with '>') -> Colocar punto final DESPUÉS de las comillas angulares: «...».
        if ($t.StartsWith(">")) {
            $qClean = $t -replace '^\s*>\s*', '' -replace '^[\s\*«\xab]+', '' -replace '[\s\*»\xbb\.]+$', ''
            $qSafe = [System.Web.HttpUtility]::HtmlEncode($qClean.Trim())
            [void]$html.Append("<blockquote class=`"epigraph`">&#171;$qSafe&#187;.</blockquote>`n")
            continue
        }

        if ($t -eq '***' -or $t -eq '---') {
            [void]$html.Append("<div class=`"scene-break`">&#10042; &#10042; &#10042;</div>`n")
            continue
        }

        if ($t -match '^[—–-]' -or $t -match '^»') {
            $cls = if ($t -match '^»') { 'dialogue-cont' } else { 'dialogue' }
            $safe = [System.Web.HttpUtility]::HtmlEncode($t)
            [void]$html.Append("<p class=`"$cls`">$safe</p>`n")
            continue
        }

        if ([string]::IsNullOrWhiteSpace($t)) { continue }

        $safe = [System.Web.HttpUtility]::HtmlEncode($t)
        [void]$html.Append("<p>$safe</p>`n")
    }

    return $html.ToString()
}

# ---- Read template ----
$template = Get-Content $tplPath -Raw -Encoding UTF8

# ---- Generate ----
foreach ($ch in $chapters) {
    if ($ch.inProgress) { continue }
    $mdPath = Join-Path $mdBase $ch.md
    if (!(Test-Path $mdPath)) { Write-Warning "Missing: $mdPath"; continue }

    $raw   = Get-Content $mdPath -Raw -Encoding UTF8
    $prose = Convert-MDBody $raw
    $sidebar = Build-Sidebar $ch.num

    $numStr = '{0:00}' -f $ch.num
    $prevSlug = if ($ch.num -gt 1)  { $chapters[$ch.num - 2].slug + '.html' } else { '../prologo.html' }
    $nextSlug = if ($ch.num -lt 13) { $chapters[$ch.num].slug + '.html' } else { '../index.html' }
    $prevText = if ($ch.num -gt 1)  { "Cap. $($ch.num - 1)" } else { 'Prologo' }
    $nextText = if ($ch.num -lt 13) { "Cap. $($ch.num + 1)" } else { 'Indice' }
    $dispTitle = $displayTitles[$ch.num - 1]

    $out = $template
    $out = $out.Replace('{{NUM}}',       $numStr)
    $out = $out.Replace('{{TITLE}}',     $ch.title)
    $out = $out.Replace('{{DISPTITLE}}', $dispTitle)
    $out = $out.Replace('{{PROSE}}',     $prose)
    $out = $out.Replace('{{SIDEBAR}}',   $sidebar)
    $out = $out.Replace('{{PREV_LINK}}', $prevSlug)
    $out = $out.Replace('{{NEXT_LINK}}', $nextSlug)
    $out = $out.Replace('{{PREV_TEXT}}', $prevText)
    $out = $out.Replace('{{NEXT_TEXT}}', $nextText)

    $outPath = Join-Path $outBase "$($ch.slug).html"
    [System.IO.File]::WriteAllText($outPath, $out, [System.Text.Encoding]::UTF8)
    Write-Host "OK: $($ch.slug).html"
}

Write-Host "`nDone. Files in: $outBase"
