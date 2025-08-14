# bob-14-forensic-NTY – 정렬 알고리즘 데모 (2조)

텍스트 파일에서 정수 목록을 읽어 다양한 정렬 알고리즘을 실행하고, 정렬 결과와 소요 시간을 출력하는 간단한 데모 프로젝트입니다.

### 팀원 및 담당
- 나소진: 버블 정렬 (Bubble Sort)
- 이민지: 선택 정렬 (Selection Sort)
- 안관우: 삽입 정렬 (Insertion Sort)
- 노태영: 퀵 정렬 (Quick Sort)
- 김준영: 병합 정렬 (Merge Sort), 팀 정렬 (TimSort)

### 지원 알고리즘
- 버블 정렬 `bubble`
- 선택 정렬 `selection`
- 삽입 정렬 `insertion`
- 병합 정렬 `merge`
- 퀵 정렬 `quick`
- 팀 정렬 `tim`

## 실행
프로젝트 루트에서 아래 명령을 실행합니다.
```bash
python bob-14-forensic-NTY/main.py               # 기본 입력: data.txt
python bob-14-forensic-NTY/main.py data.txt      # 파일 지정
```

## 출력 예시
```text
버블 정렬(Bubble)
정렬 결과: 1 2 3 5 7 8 10
소요 시간: 0.000123 초

선택 정렬(Selection)
정렬 결과: 1 2 3 5 7 8 10
소요 시간: 0.000097 초
...
```