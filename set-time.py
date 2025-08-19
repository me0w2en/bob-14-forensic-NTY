#!/usr/bin/env python3
import argparse, os, time, datetime

def parse_epoch(s: str) -> float:
    # "YYYY-MM-DD HH:MM:SS" 또는 epoch(float) 모두 허용
    try:
        return float(s)
    except ValueError:
        dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
        # 시스템 로컬시간 기준. UTC로 주고 싶다면 dt.replace(tzinfo=datetime.timezone.utc).timestamp()
        return dt.timestamp()

def main():
    p = argparse.ArgumentParser(description="Set atime/mtime with ns precision on XFS")
    p.add_argument("files", nargs="+")
    p.add_argument("--at", help="Access time (epoch or 'YYYY-MM-DD HH:MM:SS')")
    p.add_argument("--mt", help="Modify time (epoch or 'YYYY-MM-DD HH:MM:SS')")
    p.add_argument("--at-ns", type=int, default=0, help="Additional nanoseconds for atime")
    p.add_argument("--mt-ns", type=int, default=0, help="Additional nanoseconds for mtime")
    args = p.parse_args()

    for path in args.files:
        st = os.stat(path, follow_symlinks=False)
        at = parse_epoch(args.at) if args.at else st.st_atime
        mt = parse_epoch(args.mt) if args.mt else st.st_mtime

        # 나노초 정밀: Python 3.3+ 에서 ns 인자 사용
        at_ns = int(at)*10**9 + args.at_ns
        mt_ns = int(mt)*10**9 + args.mt_ns

        os.utime(path, ns=(at_ns, mt_ns), follow_symlinks=False)

        # 검증 출력
        st2 = os.stat(path, follow_symlinks=False)
        print(f"{path} -> A:{time.ctime(st2.st_atime)}  M:{time.ctime(st2.st_mtime)}")

if __name__ == "__main__":
    main()
