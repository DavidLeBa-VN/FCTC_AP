(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)
fun all_except_option(str, xs) =
    case xs of
	[] => NONE
      | x::xs'  => if same_string(str, x)
		   then SOME xs'
		   else
		       case ans of
			    NONE => NONE
			  | SOME ans => SOME (x :: ans)

fun get_substitutions1(xxs, str) =
    case xxs of
	[] => NONE
      | xs::xxs' =>
	let
	    val ans = get_substitution1(xxs', str)
	in
	    case all_except_option(str, xs) of
		NONE => ans
	      | SOME a => a @ ans

fun get_substitutions2(xxs, str) =
    let
	fun aux(xxs, str, acc) =
	    case xxs of
		[] => acc
	      | x :: xxs' => case all_except_option(str, xxs) of
				NONE => aux(xxs', str, acc)
			      | SOME ans => aux(xs', s, ans @ acc)
    in
	aux(xxs, str, [])
    end
	
fun similar_names(substitutions, name) =
    let
	val {first = x1, middle = x2, last = x3} = name
	fun get_names xs =
	    case xs of
		[] => []
	      | x :: xs' => {first = x, middle = x2, last = x3} :: (get_names(xs'))
    in
	name::get_names(get_substitutions2(substitutions, x1))
    end						    
		       

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
fun card_color(S, _) =
    case S of
	Spades => Black
      | Clubs => Black
      | _ => Red

fun card_value(_, R) =
    case R of
	Num n => n
      | Ace => 11
      | _ => 10
