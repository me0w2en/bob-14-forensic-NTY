import argparse
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
	raise NotImplementedError


def selection_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Selection Sort."""
	raise NotImplementedError


def insertion_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Insertion Sort."""
	raise NotImplementedError


def merge_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Merge Sort."""
	raise NotImplementedError


def quick_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Quick Sort."""
	raise NotImplementedError


def heap_sort(values: List[int]) -> List[int]:
	"""Return a new list sorted with Heap Sort."""
	raise NotImplementedError


SORT_ALGORITHMS: dict[str, Callable[[List[int]], List[int]]] = {
	"bubble": bubble_sort,
	"selection": selection_sort,
	"insertion": insertion_sort,
	"merge": merge_sort,
	"quick": quick_sort,
	"heap": heap_sort,
}


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Sorting demo: reads integers from data.txt and sorts them with the chosen algorithm.",
	)
	parser.add_argument(
		"--file",
		dest="file_path",
		default="data.txt",
		help="Input text file path (default: data.txt)",
	)
	parser.add_argument(
		"--algo",
		choices=sorted(SORT_ALGORITHMS.keys()),
		default="quick",
		help="Sorting algorithm to use",
	)
	parser.add_argument(
		"--limit",
		type=int,
		default=MAX_ITEMS,
		help=f"Maximum number of items to read (default: {MAX_ITEMS})",
	)
	parser.add_argument(
		"--print",
		dest="do_print",
		action="store_true",
		help="Print sorted result to stdout",
	)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	values = read_numbers_from_file(args.file_path, max_items=args.limit)
	sort_func = SORT_ALGORITHMS[args.algo]
	sorted_values = sort_func(values)
	if args.do_print:
		print(" ".join(str(x) for x in sorted_values))


if __name__ == "__main__":
	main()


