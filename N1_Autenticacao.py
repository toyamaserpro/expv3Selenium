#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Marcelo Costa Toyama -mctoyama@gmail.com 2014

# auxiliary functions for selenium CTs

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import selenium.common.exceptions

#
# N1 - Autenticação
# 

import couchdb
import aux

# all testes for autenticacao module
def allTests(logger):
    CTV3_1(logger)
    CTV3_41(logger)
    CTV3_43(logger)
    CTV3_44(logger)
    CTV3_45(logger)
    CTV3_46(logger)
    CTV3_47(logger)
    CTV3_48(logger)

# CTV3-1:Logar no sistema com sucesso
def CTV3_1(logger):

    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],doc['username'],doc['passwd'],doc['lastName'])

        logger.save('CTV3_1',"True")

    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_1(logger)
        else:
            logger.save('CTV3_1',str(err))
    finally:
        driver.quit()


# CTV3-41:Logar no sistema com login incorreto
def CTV3_41(logger):

    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],doc['username']+"WRONG",doc['passwd'],None)

        logger.save('CTV3_41',"True")
        
    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_41(logger)
        else:
            logger.save('CTV3_41',str(err))
    finally:
        driver.quit()

# CTV3-43:Logar no sistema com senha incorreta
def CTV3_43(logger):
    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],doc['username'],doc['passwd']+"WRONG",None)

        logger.save('CTV3_43',"True")
        
    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_43(logger)
        else:
            logger.save('CTV3_43',str(err))
    finally:
        driver.quit()

# CTV3-44:Logar no sistema com login vazio
def CTV3_44(logger):
    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],'',doc['passwd'],None)

        logger.save('CTV3_44',"True")
        
    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_44(logger)
        else:
            logger.save('CTV3_44',str(err))
    finally:
        driver.quit()
    

# CTV3-45:Logar no sistema com senha vazia
def CTV3_45(logger):
    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],doc['username'],'',None)

        logger.save('CTV3_45',"True")
        
    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_45(logger)
        else:
            logger.save('CTV3_45',str(err))
    finally:
        driver.quit()
    
# CTV3-46:Logar no sistema com login usando caracteres em branco
def CTV3_46(logger):
    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],'      ',doc['passwd'],None)

        logger.save('CTV3_46',"True")
        
    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_46(logger)
        else:
            logger.save('CTV3_46',str(err))
    finally:
        driver.quit()
    

# CTV3-47:Logar no sistema com senha usando caracteres em branco
def CTV3_47(logger):
    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],doc['username'],'        ',None)

        logger.save('CTV3_47',"True")
        
    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_47(logger)
        else:
            logger.save('CTV3_47',str(err))
    finally:
        driver.quit()

# CTV3-48:Logar no sistema com login usando caracteres especiais
def CTV3_48(logger):
    try:

        # Create a new instance of the webdriver        
        driver = aux.createWebDriver()

        server = couchdb.Server()
        db = server['test']
        doc = db['config']
        
        aux.login(driver,doc['url'],doc['language'],u'#9@9&,!9.á;9',doc['passwd'],None)

        logger.save('CTV3_48',"True")
        
    except Exception as err:
        if type(err) == selenium.common.exceptions.StaleElementReferenceException:
            driver.close()
            CTV3_48(logger)
        else:
            logger.save('CTV3_48',str(err))
    finally:
        driver.quit()
