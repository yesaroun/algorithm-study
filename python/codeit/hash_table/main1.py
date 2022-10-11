from HDLL1 import LinkedList    # 해시 테이블에서 사용할 링크드 리스트 임포트

class HashTable:
    """해시 테이블 클래스"""

    def __init__(self, capacity):
        self._capacity = capacity   # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]     #파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이어야 한다.
        """
        return hash(key) % self._capacity

    def look_up_value(self, key):
        """주어진 key에 해당하는 데이터를 리턴하는 메소드"""
        hash_num = self._hash_function(key)
        iterator = self._table[hash_num].head

        while iterator is not None:
            if iterator.key is key:
                return iterator.value
            iterator = iterator.next

        return None

    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다.
        """
        hash_num = self._hash_function(key)
        iterator = self._table[hash_num].head

        while iterator is not None:
            if iterator.key is key:
                iterator.value = value

        if iterator.key is not key:
            iterator.append(key, value)