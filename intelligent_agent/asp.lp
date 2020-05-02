#include <incmode>.

#program base.
% Define
location(node_a).
location(node_a).
location(node_b).
location(node_c).
location(node_d).
location(node_e).
location(node_f).
connection(node_a, node_b, 1, 1).
connection(node_a, node_c, 1, 2).
connection(node_b, node_c, 1, 1).
connection(node_c, node_d, 1, 1).
connection(node_d, node_e, 1, 1).
connection(node_e, node_f, 1, 1).

location(X) :- block(X).
holds(F,0) :- init(F).

#program step(t).
% Generate
{ move(X,M,Y,t,W,C) : block(X), location(Y), location(M) } :- holds(on(X,M),t-1), connection(M, Y, W, C).
% Test

:- move(X,M,Y,t,W,C), holds(on(A,X),t-1).
:- move(X,M,Y,t,W,C), holds(on(B,Y),t-1), B != X, Y != node_a.

:- move(X,M,Y,t,W,C), connection(M, Y, W1, C), connection(M1, Y, W2, C1), C > C1.

% Define
moved(X,t) :- move(X,M,Y,t,W,C).
holds(on(X,Y),t) :- move(X,M,Y,t,W,C).
holds(on(X,Z),t) :- holds(on(X,Z),t-1), not moved(X,t).

#program check(t).
% Test
:- query(t), goal(F), not holds(F,t).
#minimize { W: move(X,M,Y,t,W,C)}.
% Display
#show move/6.

#program base.
% Sussman Anomaly
%
block(b0).
%
init(on(b0,node_a)).
%
goal(on(b0,node_f)).
