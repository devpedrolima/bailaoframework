import xml.etree.ElementTree as ET

# Leitura do arquivo XML
tree = ET.parse('prova.xml')
root = tree.getroot()

# Criação do arquivo HTML
with open('view.html', 'w', encoding="utf-8") as f:
    # Dados do aluno
    aluno = root.find('aluno')
    nome = aluno.get('nome')
    matric = aluno.get('matric')

    # Cabeçalho do arquivo HTML
    f.write('''
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Prova de {0}</title>
</head>
<body>
 <style>
      @import url(https://fonts.googleapis.com/css?family=Merriweather:300,300italic,400,400italic|Open+Sans:800); body { font-family: sans-serif; } label{text-align: justify; font-family: "roboto"; color:#F2F2F7;} .bt { color: #007AFF; background-color: #F2F2F7; border-radius: 50px; border: 1px solid #F2F2F7; display: inline-block; cursor: pointer; font-family: Verdana; font-weight: bold; font-size: 13px; padding: 8px 15px; text-decoration: none; margin-top: 15px; } h2 {font-family: "roboto"; color:#F2F2F7;} p{font-family: "roboto"; color:#F2F2F7;} h1 { font-family: "roboto"; color:#F2F2F7; }body {background-image: url("https://4kwallpapers.com/images/wallpapers/macos-ventura-macos-13-macos-2022-stock-dark-mode-5k-retina-5120x2880-8133.jpg"); background-repeat: no-repeat; background-size: cover; !important;}.wrapper {	border-radius:20px; max-width: 800px; padding: 15px 35px 45px; margin: 0 auto;background: rgba( 41, 41, 41, 0.25 ); box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 ); backdrop-filter: blur( 11.5px ); -webkit-backdrop-filter: blur( 11.5px ); border-radius: 10px; border: 1px solid rgba( 255, 255, 255, 0.18 );margin-top: 80px;margin-bottom: 80px;}
    </style>
  <h2>Aluno: {0}</h2>
'''.format(nome))

    # Questões da prova
    questoes = root.find('QUESTOES')
    for questao in questoes:
        id_questao = questao.get('id')
        gabarito = questao.find("GABARITO").text
        enunciado = questao.find('ENUN').text
        tipo = questao.get('tipo')
        f.write('''
  <div class="questao">
    <p class="enunciado">{0}. {1}</p>
'''.format(id_questao, enunciado))
        for alternativa in questao.findall('ALT'):
            id_alt = alternativa.get('id')
            texto_alt = alternativa.text
            f.write('''
    <div class="alternativa">
      <input type="radio" name="{0}" value="{1}">
      <label for="{0}-{1}">{2}) {3}</label>
    </div>
'''.format(id_questao, id_alt, id_alt, texto_alt))
        f.write('''
    <input type="hidden" name="gabarito-{0}" gabarito="{1}">
  </div>
'''.format(id_questao, gabarito))
    # Botão de correção
    f.write('''
  <button class="bt" onclick="corrigir()">Corrigir</button>
  
  <div class="nota" id="nota"></div>
''')
    # Script de correção
    f.write('''
<script>
function corrigir(){{
  var nota = 0;\n
  for (var i = 1; i <= {0}; i++)
  {{
    var resposta = document.getElementsByName(i.toString());
    var gabarito = document.getElementsByName("gabarito-" + i.toString())[0].getAttribute("gabarito");
    for (var j = 0; j < resposta.length; j++) {{
      if (resposta[j].checked) {{
        if (resposta[j].value == gabarito)
        {{
          nota++;
        }}
        break;
      }}
    }}
  }}
  alert("Nota:" + nota + "/{0}")
}}
</script>
</body>
</html>'''.format(id_questao))