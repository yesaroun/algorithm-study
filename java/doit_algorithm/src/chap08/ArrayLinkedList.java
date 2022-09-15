// 연결 리스트 클래스(배열 커서 버전)

package chap08;

public class ArrayLinkedList<E> {

    // 노드
    class Node<E> {
        private E data;     // 데이터
        private int next;   // 리스트의 뒤쪽 포인터
        private int dnext;  // 프리 리스트의 뒤쪽 포인터

        // data와 next를 설정
        void set(E data, int next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E>[] n;        // 리스트 본체
    private int size;           // 리스트의 용량(가장 큰 데이터 수)
    private int max;            // 사용 중인 꼬리 record
    private int head;           // 머리 노드
    private int crnt;           // 선택 노드
    private int deleted;        // 프리 리스트의 머리 노드
    private static final int NULL = -1;     // 다음 노드 없음 / 리스트가 가득 참

    // 생성자
    public ArrayLinkedList(int capacity) {
        head = crnt = max = deleted = NULL;
        try {
            n = new Node[capacity];
            for (int i = 0; i < capacity; i++)
                n[i] = new Node<E>();
            size = capacity;
        }
        catch (OutOfMemoryError e) {        // 배열 생성에 실패
            size = 0;
        }
    }

    // 다음에는 삽입하는 record의 인덱스를 구함
    private int getInsertIndex() {
        if (deleted == NULL) {              // 삭제할 record가 없음
            if (max < size)
                return ++max;               // 새 record를 사용
            else
                return NULL:                // 용량 넘침(over)
        } else {
            int rec = deleted               // 프리 리스트에서
            deleted = n[rec].dnext;         // 머리 rec을 꺼냄
            return rec;
        }
    }

    // record idx 를 프리 리스트에 등록
    private void deleteIndex(int idx) {
        if (deleted == NULL) {              // 삭제할 record가 없음
            deleted = idx;                  // idx를 프리 리스트의
        }
    }
}
