# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type 
import hashlib


class Node:
    """해시를 구성하는 노드"""
    
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key      # 키
        self.value = value  # 값
        self.next = next    # 뒤쪽 노드를 참조
        

class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    
    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트)를 선언
        