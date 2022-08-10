# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = map(int, input().split())

reverse_A = int(str(A)[::-1]) 
reverse_B = int(str(B)[::-1]) 

print(max(reverse_A, reverse_B))