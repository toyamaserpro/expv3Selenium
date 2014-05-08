#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Marcelo Costa Toyama -mctoyama@gmail.com 2014

# auxiliary functions for selenium CTs

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import selenium.webdriver.common.action_chains
import selenium.common.exceptions

#
# N4 - Mensagens de email
# 

import datetime

import cfgDB
import aux
import expressomailModule

#############################################################
# all tests for this module
def allTests(mainCfg,logger):
    CTV3_7(mainCfg,logger)
    CTV3_8(mainCfg,logger)
    CTV3_11(mainCfg,logger)
    CTV3_18(mainCfg,logger)
    CTV3_20(mainCfg,logger)
    CTV3_31(mainCfg,logger)
    CTV3_506(mainCfg,logger)
    CTV3_522(mainCfg,logger)

#############################################################
#CTV3-7:Enviar Mensagens da pasta "Drafts"

def CTV3_7(mainCfg,logger):

    try:
        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)

        aux.login(mainCfg,driver)

        msg = cfgDB.getDict('CTV3_7_param.xml')

        # clica no botão compor msg e espera a janela abrir
        expressomailModule.clickCompose(mainCfg,driver,'CTV3_7_param.xml')

        # preenche campo Subject
        subjectConstant = expressomailModule.fillSubject(mainCfg,driver,'CTV3_7_param.xml')

        # preenche campo body
        expressomailModule.fillBody(mainCfg,driver,'CTV3_7_param.xml')
        
        # click salvar rascunho
        expressomailModule.clickSaveDraft(mainCfg,driver,'CTV3_7_param.xml')

        # checar mensagem por assunto na pasta draft
        expressomailModule.clickFolder(mainCfg,driver,"Rascunhos")
        msgEl = expressomailModule.elementInFolder(mainCfg,driver,subjectConstant)

        action = selenium.webdriver.common.action_chains.ActionChains(driver)
        action.double_click( msgEl )
        action.perform()

        # switch to compose window
        windowCompose = None

        WebDriverWait(driver, mainCfg['timeout']).until( lambda driver: len(driver.window_handles) == 2 )

        windowCompose = driver.window_handles[-1]
        driver.switch_to_window(windowCompose)
        WebDriverWait(driver, mainCfg['timeout']).until(EC.title_contains('Compor mensagem:'))
            
        # filling TO field
        expressomailModule.fillToOption(mainCfg,driver,'CTV3_7_param.xml','TO')

        # clicking send
        expressomailModule.clickSend(mainCfg,driver,'CTV3_7_param.xml',windowCompose)

        logger.save('CTV3_7','Enviar Mensagens da pasta "Drafts"','True')        

    except Exception as err:
        logger.save('CTV3_7','Enviar Mensagens da pasta "Drafts"',str(type(err))+str(err))

    finally:
        driver.quit()


#############################################################
# CTV3-8:Criar Mensagem apenas com To
def CTV3_8(mainCfg,logger):

    try:
        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)

        aux.login(mainCfg,driver)

        window = expressomailModule.clickCompose(mainCfg,driver,'CTV3_8_param.xml')
        expressomailModule.fillToOption(mainCfg,driver,'CTV3_8_param.xml',"TO")
        expressomailModule.fillSubject(mainCfg,driver,'CTV3_8_param.xml')
        expressomailModule.fillBody(mainCfg,driver,'CTV3_8_param.xml')
        expressomailModule.clickSend(mainCfg,driver,'CTV3_8_param.xml',window)

        logger.save('CTV3_8','Criar Mensagem apenas com To','True')        

    except Exception as err:
        logger.save('CTV3_8','Criar Mensagem apenas com To',str(type(err))+str(err))

    finally:
        driver.quit()

#############################################################
# CTV3-11:Criar Mensagem apenas com Cc
def CTV3_11(mainCfg,logger):

    try:
        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)
        aux.login(mainCfg,driver)
        window = expressomailModule.clickCompose(mainCfg,driver,'CTV3_11_param.xml')
        expressomailModule.fillToOption(mainCfg,driver,'CTV3_11_param.xml','Cc')
        expressomailModule.fillSubject(mainCfg,driver,'CTV3_11_param.xml')
        expressomailModule.fillBody(mainCfg,driver,'CTV3_11_param.xml')
        expressomailModule.clickSend(mainCfg,driver,'CTV3_11_param.xml',window)

        logger.save('CTV3_11','Criar Mensagem apenas com Cc','True') 

    except Exception as err:
        logger.save('CTV3_11','Criar Mensagem apenas com Cc',str(type(err))+str(err))        

    finally:
        driver.quit()

#############################################################
# CTV3-18:Excluir mensagem selecionada
def CTV3_18(mainCfg,logger):
    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)

        msg = cfgDB.getDict('CTV3_18_param.xml')

        # login
        aux.login(mainCfg,driver)

        # compose mail
        window = expressomailModule.clickCompose(mainCfg,driver,'CTV3_18_param.xml')
        expressomailModule.fillToOption(mainCfg,driver,'CTV3_18_param.xml',"TO")
        subjectConstant = expressomailModule.fillSubject(mainCfg,driver,'CTV3_18_param.xml')
        expressomailModule.fillBody(mainCfg,driver,'CTV3_18_param.xml')
        expressomailModule.clickSend(mainCfg,driver,'CTV3_18_param.xml',window)

        # delete mail
        expressomailModule.clickFolder(mainCfg,driver,"Entrada")
        msgSubjectList = expressomailModule.listFolderMessagesSubject(mainCfg,driver)

        if subjectConstant in msgSubjectList:
            
            if expressomailModule.selectMessageInFolder(mainCfg,driver,subjectConstant):
                if not expressomailModule.clickDelete(mainCfg,driver,subjectConstant):
                    raise Exception('Could not delete message: '+msg['SUBJECT'])
            else:
                raise Exception('Could not select the message: '+msg['SUBJECT'])

        else:
            raise Exception('subject '+msg['SUBJECT']+' is not present in INBOX')

        logger.save('CTV3_18','Excluir mensagem selecionada','True')

    except Exception as err:
        logger.save('CTV3_18','Excluir mensagem selecionada',str(type(err))+str(err))

    finally:
        driver.quit()


#############################################################
# CTV3-20:Excluir mensagem aberta

def CTV3_20(mainCfg,logger):

    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)

        msg = cfgDB.getDict('CTV3_20_param.xml')

        # login
        aux.login(mainCfg,driver)

        # compose mail
        window = expressomailModule.clickCompose(mainCfg,driver,'CTV3_20_param.xml')
        expressomailModule.fillToOption(mainCfg,driver,'CTV3_20_param.xml',"TO")
        subjectConstant = expressomailModule.fillSubject(mainCfg,driver,'CTV3_20_param.xml')
        expressomailModule.fillBody(mainCfg,driver,'CTV3_20_param.xml')
        expressomailModule.clickSend(mainCfg,driver,'CTV3_20_param.xml',window)

        # delete mail
        expressomailModule.clickFolder(mainCfg,driver,"Entrada")
        msgSubjectList = expressomailModule.listFolderMessagesSubject(mainCfg,driver)

        if subjectConstant in msgSubjectList:

            # open msg in new window
            window = expressomailModule.openMessageInFolder(mainCfg,driver,subjectConstant)

            if window is None:
                raise Exception('Could not open message: '+msg['SUBJECT'])
            else:
                # click delete in opened message
                expressomailModule.clickDeleteInOpenedMessage(mainCfg,driver,window)

        logger.save('CTV3_20','Excluir mensagem aberta','True')


    except Exception as err:
        logger.save('CTV3_20','Excluir mensagem aberta',str(type(err))+str(err))        

    finally:
        driver.quit()

#############################################################
# CTV3-31:Enviar Mensagens
def CTV3_31(mainCfg,logger):

    try:
        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)

        aux.login(mainCfg,driver)

        window = expressomailModule.clickCompose(mainCfg,driver,'CTV3_31_param.xml')
        expressomailModule.fillToOption(mainCfg,driver,'CTV3_31_param.xml',"TO")
        expressomailModule.fillSubject(mainCfg,driver,'CTV3_31_param.xml')
        expressomailModule.fillBody(mainCfg,driver,'CTV3_31_param.xml')
        expressomailModule.clickSend(mainCfg,driver,'CTV3_31_param.xml',window)

        logger.save('CTV3_31','Enviar Mensagens','True')        

    except Exception as err:
        logger.save('CTV3_31','Enviar Mensagens',str(type(err))+str(err))

    finally:
        driver.quit()
#############################################################
#CTV3-506:Excluir todas as mensagens de uma pasta
def CTV3_506(mainCfg,logger):
    try:
        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)

        msg = cfgDB.getDict('CTV3_506_param.xml')
        
        aux.login(mainCfg,driver)

        # opening folder
        expressomailModule.clickFolder(mainCfg,driver,msg['folderName'])

        # the accont must hae at least one message for deletion
        if len(expressomailModule.listFolderMessagesSubject(mainCfg,driver)) == 0:
            raise Exception('Must have at least one message for deletion!')

        # selecting all from page
        expressomailModule.selectAllFromPage(mainCfg,driver)

        if not expressomailModule.clickDelete(mainCfg,driver,None):
            raise Exception('Could not delete page')

        logger.save(u'CTV3_506',u'Excluir todas as mensagens de uma pasta',u'True')

    except Exception as err:
        logger.save('CTV3_506','Excluir todas as mensagens de uma pasta',str(type(err))+str(err))        
    finally:
        driver.quit()

#############################################################
#CTV3-522:Salvar MENSAGEM rascunho sem destinatário

def CTV3_522(mainCfg,logger):

    try:
        # Create a new instance of the webdriver        
        driver = aux.createWebDriver(mainCfg)

        msg = cfgDB.getDict('CTV3_522_param.xml')
        
        aux.login(mainCfg,driver)

        # click compose msg
        expressomailModule.clickCompose(mainCfg,driver,'CTV3_522_param.xml')

        # filling subject field
        subjectConstant = expressomailModule.fillSubject(mainCfg,driver,'CTV3_522_param.xml')

        # filling email body
        expressomailModule.fillBody(mainCfg,driver,'CTV3_522_param.xml')

        # click salvar rascunho
        expressomailModule.clickSaveDraft(mainCfg,driver,'CTV3_522_param.xml')

        # checando se a mensagem foi salva na pasta draft
        expressomailModule.clickFolder(mainCfg,driver,"Rascunhos")
        expressomailModule.elementInFolder(mainCfg,driver,subjectConstant)

        logger.save(u'CTV3_522',u'Salvar MENSAGEM rascunho sem destinatário',u'True')

    except Exception as err:
        logger.save(u'CTV3_522',u'Salvar MENSAGEM rascunho sem destinatário',str(type(err))+str(err))

    finally:
        driver.quit()    

#############################################################
