%%%-------------------------------------------------------------------
%% @doc erlang public API
%% @end
%%%-------------------------------------------------------------------

-module(palindrome).

-export([start/0, stop/0, is_palindrome/1]).

start() ->
    io:format("dad: ~p~n", [is_palindrome("dad")]),
    io:format("mom: ~p~n", [is_palindrome("mom")]),
    io:format("moon: ~p~n", [is_palindrome("moon")]),

    io:format("Try entering a word! We'll see if it's a palindrome: "),
    Input = io:get_line(""),
    Answer = is_palindrome(Input),
    create_statement(Answer),

    stop().

stop() ->
    ok.

create_statement(Answer) ->
    case Answer of
        true -> io:format("Congrats! That one's a palindrome!~n");
        false -> io:format("That one isn't a palindrome.~n")
    end.

first_letter(Word) ->
    string:slice(Word, 0, 1).
last_letter(Word) ->
    string:slice(Word, length(Word)-1,1).
middle_letters(Word) ->
    string:slice(Word, 1, length(Word)-2).

is_palindrome(Word) when length(Word) < 2 ->
    true;
is_palindrome(Word) when length(Word) == 2  ->
    first_letter(Word) == last_letter(Word);
is_palindrome(Word) ->
    case first_letter(Word) == last_letter(Word) of
        true -> is_palindrome(middle_letters(Word));
        false -> false
    end.