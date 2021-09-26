;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname Study_File) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(list "a" "b")
(list 1 "a")

(define L1 (list "a" "b"))
(define L2 (list 1 "a"))

(cons "a" L1)
(list "a" L1)

(cons L1 L2)

(append L1 L2)
