;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname study_file) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(map positive? (list 1 2 3))
(map sqr (list 1 2 3))
;(map (+ 1) (list 1 2 3))

(foldr + 0 (list 1 2 4))
(foldr * 2 (list 1 2 4))

(filter negative? (list 1 -2 3))
(filter string? (list 1 -2 3))
(filter integer? (list 1 -2 3))
(filter positive? (list 1 -2 3))

(identity (+ 3 4))
(build-list 3 identity)
(build-list 3 sqr)
(build-list 3 sqrt)


