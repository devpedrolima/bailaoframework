#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:38:53 2023

@author: adrianobailao
"""

import xml.etree.ElementTree as ET

class Prova:
    
  def __init__(self, prova):
    
    tree = ET.parse(prova)
    self.root = tree.getroot()

  def myfunc(self):
    print(self.root)
    
  def todos(self):
      for child in self.root:
          print(child.tag, child.attrib)
          
  def todos2(self):
      for child in self.root.findall('aluno'):
          print(child.text)
          
  def saida(self):
    arquivo = open('./interface/view.html', 'w')
    arquivo.writelines('<HTML><HEAD></HEAD><BODY><STYLE>@import url(https://fonts.googleapis.com/css?family=Merriweather:300,300italic,400,400italic|Open+Sans:800); body { font-family: sans-serif; } label{text-align: justify; font-family: "roboto"; color:#F2F2F7;} .bt { color: #007AFF; background-color: #F2F2F7; border-radius: 50px; border: 1px solid #F2F2F7; display: inline-block; cursor: pointer; font-family: Verdana; font-weight: bold; font-size: 13px; padding: 8px 15px; text-decoration: none; margin-top: 15px; } h2 {font-family: "roboto"; color:#F2F2F7;} p{font-family: "roboto"; color:#F2F2F7;} h1 { font-family: "roboto"; color:#F2F2F7; }body {background-image: url("https://4kwallpapers.com/images/wallpapers/macos-ventura-macos-13-macos-2022-stock-dark-mode-5k-retina-5120x2880-8133.jpg"); background-repeat: no-repeat; background-size: cover; !important;}.wrapper {	border-radius:20px; max-width: 800px; padding: 15px 35px 45px; margin: 0 auto;background: rgba( 41, 41, 41, 0.25 ); box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 ); backdrop-filter: blur( 11.5px ); -webkit-backdrop-filter: blur( 11.5px ); border-radius: 10px; border: 1px solid rgba( 255, 255, 255, 0.18 );margin-top: 80px;margin-bottom: 80px;}</STYLE> <div class="wrapper">')

    title_element = self.root.find('aluno')

    nome = title_element.attrib['nome']
    nome_do_aluno = '<H1> Aluno: ' + nome + '</H1>'
    arquivo.writelines(nome_do_aluno)

    matricula = title_element.attrib['matricula']
    matricula_do_aluno = '<H2> Matricula: ' + matricula + '</H2>'
    arquivo.writelines(matricula_do_aluno)

    # Define um contador para o id dos inputs de cada questão
    contador_input = 1

    questoes = self.root.findall('.//questao')

    # Percorre cada elemento QUESTAO encontrado
    for questao in questoes:
        id_questao = questao.attrib['id']

        enunciado = questao.find('enun').text
        arquivo.writelines('<p>' + id_questao + ') ' + enunciado + '</p>')

        # Define um nome para os inputs da questão
        nome_input_questao = 'questao_' + id_questao

        alternativas = questao.findall('alt')
        for alternativa in alternativas:
            # Acessa o atributo id da alternativa
            id_alternativa = alternativa.attrib['id']
            # Acessa o texto da alternativa
            texto_alternativa = alternativa.text
            
            # Cria o input do tipo radio para a alternativa
            input_alternativa = f'<input type="radio" name="{nome_input_questao}" id="{contador_input}" value="{id_alternativa}">'
            # Adiciona o input à página HTML
            arquivo.writelines(input_alternativa)

            # Adiciona o texto da alternativa à página HTML
            arquivo.writelines(f'<label for="{contador_input}">{texto_alternativa}</label><br>')
            
         
            contador_input += 1

   
    arquivo.writelines('<button class="bt" onclick="conferir()">Enviar</button>')



    arquivo.writelines('<script>\n')
    arquivo.writelines('function conferir() {\n')
    arquivo.writelines('\tvar respostas = document.getElementsByName("resposta");\n')
    arquivo.writelines('\tvar acertos = 0;\n')
    arquivo.writelines('\tvar erros = 0;\n')
    arquivo.writelines('\tfor (var i = 0; i < respostas.length; i++) {\n')
    arquivo.writelines('\t\tif (respostas[i].checked && respostas[i].value === gabarito[i]) {\n')
    arquivo.writelines('\t\t\tacertos++;\n')
    arquivo.writelines('\t\t} else {\n')
    arquivo.writelines('\t\t\terros++;\n')
    arquivo.writelines('\t\t}\n')
    arquivo.writelines('\t}\n')
    arquivo.writelines('\tvar total = acertos + erros;\n')
    arquivo.writelines('\tvar porcentagem = acertos / total * 100;\n')
    arquivo.writelines('\talert("Você acertou " + acertos + " questões e errou " + erros + " questões. Sua porcentagem de acerto é de " + porcentagem.toFixed(2) + "%.");\n')
    arquivo.writelines('}\n')
    arquivo.writelines('</script>\n')



    arquivo.writelines('</div></BODY></HTML>')
    arquivo.close()