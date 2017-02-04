#!/usr/bin/env python3
# coding=utf-8
import time, datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from nose.tools import *

def setup(self):
    self.browser = webdriver.Chrome("/home/kyle/bin/chromedriver")
    self.browser.implicitly_wait(10)
    self.browser.maximize_window()
    now = datetime.datetime.now()
    now_time = now.strftime("%m%d%H%M")
    self.username = "n" + now_time
    self.password = "test1234"
    self.topic_name = "test-topic"
    self.entry_name = "test-entry"

def test_case_register():
    browser.get("http://localhost:8000/")
    browser.find_element_by_link_text("注册").click()
    browser.find_element_by_id("id_username").send_keys(username)
    browser.find_element_by_id("id_password1").send_keys(password)
    browser.find_element_by_id("id_password2").send_keys(password)
    browser.find_element_by_name("submit").click()
    WebDriverWait(browser, 2).until(
        lambda driver: driver.find_element_by_tag_name('body'))
    assert_equal(browser.find_element_by_link_text("注销").text, '注销')
    assert_equal(browser.find_element_by_partial_link_text("Hi").text, 'Hi, ' + username)

def test_case_logout():
    browser.find_element_by_link_text("注销").click()
    assert_equal(browser.find_element_by_link_text("登录").text, '登录')

def test_case_topic_list_logout():
    browser.find_element_by_link_text("主题列表").click()
    assert_equal(browser.find_element_by_name("submit").text, '登录')

def test_case_login():
    browser.find_element_by_link_text("登录").click()
    browser.find_element_by_id("id_username").send_keys(username)
    browser.find_element_by_id("id_password").send_keys(password)
    browser.find_element_by_name("submit").click()
    assert_equal(browser.find_element_by_link_text("注销").text, '注销')
    assert_equal(browser.find_element_by_partial_link_text("Hi").text, 'Hi, ' + username)
    
def test_case_topic_list_log_in():
    browser.find_element_by_link_text("主题列表").click()
    assert_equal(browser.find_element_by_link_text("新增主题").text, '新增主题')

def test_case_new_topic():
    browser.find_element_by_link_text("新增主题").click()
    browser.find_element_by_id("id_text").send_keys(topic_name)
    browser.find_element_by_name("submit").click()
    assert_equal(browser.find_element_by_link_text(topic_name).text, topic_name)

def test_case_new_entry():
    browser.find_element_by_link_text(topic_name).click()
    browser.find_element_by_link_text("新增条目").click()
    browser.find_element_by_id("id_text").send_keys(entry_name)
    browser.find_element_by_name("submit").click()
    assert_equal(browser.find_element_by_link_text("编辑条目").text, "编辑条目")
    assert_equal(browser.find_element_by_class_name("panel-body").text, entry_name)

def test_case_edit_entry():
    browser.find_element_by_link_text("编辑条目").click()
    browser.find_element_by_id("id_text").send_keys("条目编辑后")
    browser.find_element_by_name("submit").click()
    assert_equal(browser.find_element_by_class_name("panel-body").text, 
                 entry_name + "条目编辑后")

def test_case_home_page():
    browser.find_element_by_link_text("主页").click()
    browser.find_element_by_link_text("注册新账号").click()
    assert_equal(browser.find_element_by_name("submit").text, '注册')

def teardown():
    browser.quit()
