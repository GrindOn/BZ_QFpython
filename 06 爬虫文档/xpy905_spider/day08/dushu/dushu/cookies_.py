#!/usr/bin/python3
# coding: utf-8
import random

cookie_list = [
    '_lxsdk_cuid=16f5a716017c8-00ff0f000ceb74-1d376b5b-fa000-16f5a716018c8; _lxsdk=16f5a716017c8-00ff0f000ceb74-1d376b5b-fa000-16f5a716018c8; _hc.v=5cd08a7b-be63-5879-64be-bc4cb0c75ae2.1577770378; cy=17; cye=xian; s_ViewType=10; thirdtoken=c76e5618-808f-40b4-ac63-29ae65340dad; _thirdu.c=a7c1f404ff63ab616e9bafe4f8b01ed1; ll=7fd06e815b796be3df069dec7836c3df; ua=disen; ctu=a4a4e347545841e540c860c34199e51fe426475ece09677185a58e3d3045b11b; dper=eabd9e0f4d6bcf62aadb096fb761b7734ecc60c046749b73b4408c8b3cc5e4f81ac9539163579c2e1ffac2159bab6b671b402ca1b601dc68aa1f1ee7f989fbc376b8d776f68ec84e91af59e41e36f1da9fba74976e13783c51a26f9a5c7fd2b7; uamo=17791692095; _lxsdk_s=16f6496f1a8-d1b-1f2-c20%7C%7C310'
]

def cookie():
    co = random.choice(cookie_list)
    return {
         key.strip(): value.strip()
         for key, value in
         [
           item.split('=')
           for item in co.split(';')
         ]
     }

if __name__ == '__main__':
    print(cookie())