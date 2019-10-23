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

#CNPJ
botaocnpj1 = browser.find_element_by_xpath("//*[@id='rblCnpjContratante']")
botaocnpj1.click()
time.sleep(3)
cnpj1 = browser.find_element_by_xpath("//*[@id='txtCNPJ']")
cnpj1.send_keys('')

#CEP / Endereço
cep1 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCEnderecoContratante_txtCep']")
cep1.send_keys('')
botaocep1 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCEnderecoContratante_btnPesquisarCep']")
botaocep1.click()
time.sleep(10)
numero1 = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UCEnderecoContratante_txtNumero']")
numero1.send_keys('')

#Data do contrato
datacontrato = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txtDataContrato']")
datacontrato.send_keys('23/10/2019')

#Valor do contrato (Honorários)
valorhono = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txtValorContrato']")
valorhono.send_keys('200000')

#Pessoa juridica privada ou publica
tipocontratante = browser.find_element_by_xpath("//*[@id='ddlTipoContratante']")
tipocontratante.send_keys("PESSOA JURIDICA DE DIREITO PRIVADO")




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

