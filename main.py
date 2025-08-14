import argparse
import time
from typing import Callable, List


MAX_ITEMS: int = 10000


def read_numbers_from_file(file_path: str, max_items: int = MAX_ITEMS) -> List[int]:
	"""Read integers from a text file into a list (up to max_items).

	The file may contain numbers separated by spaces, newlines, or commas.
	Raises ValueError if a token cannot be parsed as an integer.
	"""
	data: List[int] = []
	with open(file_path, "r", encoding="utf-8") as f:
		buffer = f.read()
		buffer = buffer.replace(",", " ")
		tokens = buffer.split()
		for token in tokens[:max_items]:
			try:
				num = int(token)
			except ValueError as exc:
				raise ValueError(f"Invalid integer token: {token!r}") from exc
			data.append(num)
	return data


def bubble_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Bubble Sort."""
	result: List[int] = values.copy()
	n = len(result)
	if n < 2:
		return result
	for end in range(n - 1, 0, -1):
		swapped = False
		for i in range(end):
			if result[i] > result[i + 1]:
				result[i], result[i + 1] = result[i + 1], result[i]
				swapped = True
		if not swapped:
			break
	return result


def selection_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Selection Sort."""
	result: List[int] = list(values)
	n: int = len(result)
	for i in range(n - 1):
		min_index = i
		for j in range(i + 1, n):
			if result[j] < result[min_index]:
				min_index = j
		if min_index != i:
			result[i], result[min_index] = result[min_index], result[i]
	return result


def insertion_sort(values: List[int]) -> List[int]:
    """Return a new list sorted with Insertion Sort."""
    result = values.copy()  # 원본 리스트를 변경하지 않기 위해 복사
    
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        
        # key보다 큰 요소들을 한 칸씩 뒤로 이동
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        
        # key를 올바른 위치에 삽입
        result[j + 1] = key
    
    return result


def merge_sort(values: List[int]) -> List[int]:
    """Return a new list sorted with Merge Sort."""
    if len(values) <= 1:
        return values[:]  # 원본 리스트 복사

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    merged: List[int] = []
    i = j = 0

    # 두 리스트 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 남은 요소 추가
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged



def quick_sort(values: List[int]) -> List[int]:
    """Return a new list sorted with Quick Sort."""
    # 원본 리스트를 변경하지 않기 위해 복사본 사용
    arr = list(values)

    # 재귀 종료 조건: 원소가 1개 이하이면 그대로 반환
    if len(arr) <= 1:
        return arr

    # 피벗(Pivot) 선택: 중간값 사용 → 편향된 분할 방지
    pivot = arr[len(arr) // 2]

    # 피벗 기준으로 왼쪽, 중간(피벗과 동일), 오른쪽 리스트 생성
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 왼쪽과 오른쪽은 재귀적으로 정렬 후 합침
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Heap Sort."""
	raise NotImplementedError


SORT_ALGORITHMS: dict[str, Callable[[List[int]], List[int]]] = {
	"bubble": bubble_sort,
	"selection": selection_sort,
	"insertion": insertion_sort,
	"merge": merge_sort,
	"quick": quick_sort,
	"tim": tim_sort,
}


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Sorting demo: read integers from a text file and show results and timings for multiple sorting algorithms.",
	)
	parser.add_argument(
		"file_path",
		nargs="?",
		default="data.txt",
		help="Input text file path (default: data.txt)",
	)
	parser.add_argument(
		"--limit",
		type=int,
		default=MAX_ITEMS,
		help=f"Maximum number of items to read (default: {MAX_ITEMS})",
	)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	values = read_numbers_from_file(args.file_path, max_items=args.limit)

	ordered_algorithms = [
		("버블 정렬(Bubble)", "bubble"),
		("선택 정렬(Selection)", "selection"),
		("삽입 정렬(Insertion)", "insertion"),
		("병합 정렬(Merge)", "merge"),
		("퀵 정렬(Quick)", "quick"),
		("팀 정렬(tim)", "tim"),
	]

	for display_name, key in ordered_algorithms:
		sort_func = SORT_ALGORITHMS[key]
		start_time = time.perf_counter()
		sorted_values = sort_func(values)
		elapsed = time.perf_counter() - start_time

		print(display_name)
		print("정렬 결과:", " ".join(str(x) for x in sorted_values))
		print(f"소요 시간: {elapsed:.6f} 초")
		print()


if __name__ == "__main__":
	main()


