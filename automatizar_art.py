from selenium import webdriver
import time

browser = webdriver.Chrome()
page_url = "http://servicos.crea-mg.org.br/natcgi/AtendeWeb.exe/CREA/LOGINATW?tiporeg=P"
browser.get(page_url)

#Nome do usuário
usuario = browser.find_element_by_xpath("/html/body/form/table[1]/tbody/tr[3]/td[2]/input")
usuario.send_keys('')

#Senha
senha = browser.find_element_by_xpath("/html/body/form/table[1]/tbody/tr[3]/td[4]/input")
senha.send_keys('')

#Click no botão para login
login = browser.find_element_by_xpath("/html/body/form/table[1]/tbody/tr[3]/td[5]/input")
login.click()

#Página de nova ART
novaart = browser.find_element_by_xpath("//*[@id='itemMenuART']")
novaart.click()
time.sleep(5)

#Preencher Nova ART de Obra/Serviço
browser.switch_to.frame("mainWindow")
obraserv =browser.find_element_by_xpath("//*[@id='lnkObra']")
obraserv.click()
time.sleep(5)

#Empresa contratada / HLS, Elevar, RV
empresacontratada = browser.find_element_by_xpath("//*[@id='txtContratada']") 
empresacontratada.send_keys('')

#Nome do Contratante
contratante = browser.find_element_by_xpath("//*[@id='txtContratante']")
contratante.send_keys('Condominio')

#CNPJ do contratante
botaocnpj1 = browser.find_element_by_xpath("//*[@id='rblCnpjContratante']")
botaocnpj1.click()
time.sleep(3)
cnpj1 = browser.find_element_by_xpath("//*[@id='txtCNPJ']")
cnpj1.send_keys('10965925000120')

#CEP / Endereço
cep1 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCEnderecoContratante_txtCep']")
cep1.send_keys('33202810')
botaocep1 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCEnderecoContratante_btnPesquisarCep']")
botaocep1.click()
time.sleep(10)
numero1 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCEnderecoContratante_txtNumero']")
numero1.send_keys('100')

#Data do contrato
datacontrato = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txtDataContrato']")
datacontrato.send_keys('23/10/2019')

#Valor do contrato (Honorários)
valorhono = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txtValorContrato']")
valorhono.send_keys('200000')

#Pessoa juridica privada ou publica
tipocontratante = browser.find_element_by_xpath("//*[@id='ddlTipoContratante']")
tipocontratante.send_keys("PESSOA JURIDICA DE DIREITO PRIVADO")

#Data de início da obra
dataini = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txtDataInicioObraServico']")
dataini.send_keys("23/10/2019")

#Data de final da obra
datatermi = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txtPrevisaoTerminoObraServico']")
datatermi.send_keys('22/10/2020')

#Valor da obra
valorobra = browser.find_element_by_xpath("//*[@id='txtValorObra']")
valorobra.send_keys('450000')

#Finalidade do prédio
finalidade = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_ddlFinalidades']")
finalidade.send_keys("COMERCIAL")

#Proprietário do prédio
proprie = browser.find_element_by_xpath("//*[@id='txtProprietario']")
proprie.send_keys('Condominio')

#CNPJ da obra
botaocnpj2 = browser.find_element_by_xpath("//*[@id='rblCnpjProprietario']")
botaocnpj2.click()
time.sleep(3)
cnpj2 = browser.find_element_by_xpath("//*[@id='txtCnpjProprietario']")
cnpj2.send_keys('10965925000120')

#CEP / Endereço da obra
cep2 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCMenuEndereco1_endereco1_txtCep']")
cep2.send_keys('33202810')
botaocep2 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCMenuEndereco1_endereco1_btnPesquisarCep']")
botaocep2.click()
time.sleep(10)
numero2 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCMenuEndereco1_endereco1_txtNumero']")
numero2.send_keys('100')

#Cadastro do Laudo
grupoareaatuacao1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/select[1]")
grupoareaatuacao1.send_keys('ENGENHARIA INDUSTRIAL')
time.sleep(3)
nivelatuacao1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/select[2]")
nivelatuacao1.send_keys('EXECUÇÃO')
atividadeprof1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/select[3]")
atividadeprof1.send_keys('31 - LAUDO')
areaatuacao1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/select[4]")
areaatuacao1.send_keys('60 - MECANICA')
obraservico1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/select[5]")
obraservico1.send_keys('EQUIPAMENTOS - MÁQUINAS ELÉTRICOS OU ELETRÔNICOS')
time.sleep(3)
complemento1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/select[6]")
complemento1.send_keys('ELEVADORES')
quantidade1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/input")
quantidade1.send_keys('100')
unidade1 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica1_conteudo']/select[7]")
unidade1.send_keys('un - UNIDADE')

#Cadastro do serviço de manutenção do elevador
botaoincluir = browser.find_element_by_xpath("//*[@id='btnIncluirAtividadeTecnica']")
botaoincluir.click()
time.sleep(6)
grupoareaatuacao2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/select[1]")
grupoareaatuacao2.send_keys('ENGENHARIA INDUSTRIAL')
time.sleep(3)
nivelatuacao2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/select[2]")
nivelatuacao2.send_keys('EXECUÇÃO')
atividadeprof2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/select[3]")
atividadeprof2.send_keys('33 - INSTALAÇÃO/MANUTENÇÃO DE EQUIPAMENTO')
areaatuacao2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/select[4]")
areaatuacao2.send_keys('60 - MECANICA')
obraservico2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/select[5]")
obraservico2.send_keys('EQUIPAMENTOS - MÁQUINAS ELÉTRICOS OU ELETRÔNICOS')
time.sleep(3)
complemento2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/select[6]")
complemento2.send_keys('ELEVADORES')
quantidade2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/input")
quantidade2.send_keys('100')
unidade2 = browser.find_element_by_xpath("//*[@id='abaAtividadeTecnica2_conteudo']/select[7]")
unidade2.send_keys('un - UNIDADE')

#Descrição do serviço/Observações
observacoes = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txtObservacoes']")
observacoes.send_keys('Manutencao de 1 elevador')

#Estou ciente
estouciente = browser.find_element_by_xpath("//*[@id='chkLivroOrdemSim']")
estouciente.click()

#Entidade de Classe
entclasse = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_ddlEntidadeClasse']")
entclasse.send_keys('60 - SINDICATO DE ENGENHEIROS NO ESTADO DE MINAS GERAIS - SENGE-MG')


'''
 = browser.find_element_by_xpath("")
 
empresacontratada - //*[@id='txtContratada']
contratante - //*[@id='txtContratante']
botaocnpj1 - //*[@id='rblCnpjContratante']
cnpj1 - //*[@id='txtCNPJ']
cep1  - //*[@id='ContentPlaceHolder1_UCEnderecoContratante_txtCep']
botaocep1 - //*[@id='ContentPlaceHolder1_UCEnderecoContratante_btnPesquisarCep']
numero1 - //*[@id='ContentPlaceHolder1_UCEnderecoContratante_txtNumero']
datacontrato - //*[@id='ContentPlaceHolder1_txtDataContrato']
valorhono - //*[@id='ContentPlaceHolder1_txtValorContrato']
tipocontratante - //*[@id='ddlTipoContratante']
dataini - //*[@id='ContentPlaceHolder1_txtDataInicioObraServico']
datatermi - //*[@id='ContentPlaceHolder1_txtPrevisaoTerminoObraServico']
valorobra - //*[@id='txtValorObra']
finalidade - //*[@id='ContentPlaceHolder1_ddlFinalidades']
proprie - //*[@id='txtProprietario']
botaocnpj2 - //*[@id='rblCnpjProprietario']
cnpj2 - //*[@id='txtCnpjProprietario']
cep2 - //*[@id='ContentPlaceHolder1_UCMenuEndereco1_endereco1_txtCep']
botaocep2 - //*[@id='ContentPlaceHolder1_UCMenuEndereco1_endereco1_btnPesquisarCep']
numero2 - //*[@id='ContentPlaceHolder1_UCMenuEndereco1_endereco1_txtNumero']
grupoareaatuacao1 - //*[@id='abaAtividadeTecnica1_conteudo']/select[1]
nivelatuacao1 - //*[@id='abaAtividadeTecnica1_conteudo']/select[2]
atividadeprof1 - //*[@id='abaAtividadeTecnica1_conteudo']/select[3]
areaatuacao1 - //*[@id='abaAtividadeTecnica1_conteudo']/select[4]
obraservico1 - //*[@id='abaAtividadeTecnica1_conteudo']/select[5]
complemento1 - //*[@id='abaAtividadeTecnica1_conteudo']/select[6]
quantidade1 - //*[@id='abaAtividadeTecnica1_conteudo']/input
unidade1 - //*[@id='abaAtividadeTecnica1_conteudo']/select[7]
botaoincluir - //*[@id='btnIncluirAtividadeTecnica']
grupoareaatuacao2 - //*[@id='abaAtividadeTecnica2_conteudo']/select[1]
nivelatuacao2 - //*[@id='abaAtividadeTecnica2_conteudo']/select[2]
atividadeprof2 - //*[@id='abaAtividadeTecnica2_conteudo']/select[3]
areaatuacao2 - //*[@id='abaAtividadeTecnica2_conteudo']/select[4]
obraservico2 - //*[@id='abaAtividadeTecnica2_conteudo']/select[5]
complemento2 - //*[@id='abaAtividadeTecnica2_conteudo']/select[6]
quantidade2 - //*[@id='abaAtividadeTecnica2_conteudo']/input
unidade2 - //*[@id='abaAtividadeTecnica2_conteudo']/select[7]
observacoes - //*[@id='ContentPlaceHolder1_txtObservacoes']
estouciente - //*[@id='chkLivroOrdemSim']
entclasse - //*[@id='ContentPlaceHolder1_ddlEntidadeClasse']


'''

#browser.switch_to.default_content() - Sair do iframe

