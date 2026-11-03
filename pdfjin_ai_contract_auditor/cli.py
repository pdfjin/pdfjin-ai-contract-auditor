import sys
import argparse
from pathlib import Path
try:
    from .core import audit_contract
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_ai_contract_auditor.core import audit_contract
    from pdfjin_ai_contract_auditor import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="pdfjin-ai-contract-auditor",
        description="Audit contracts and legal agreements for risk clauses using AI.",
        epilog="Online web version available at https://pdfjin.com/pages/ai-contract-auditor.html",
    )
    parser.add_argument("input", metavar="INPUT_PDF", help="Path to the contract PDF")
    parser.add_argument("-o", "--output", help="Optional path to save report (default: print to stdout)")
    parser.add_argument("--key", help="Google Gemini API Key (or set GEMINI_API_KEY environment variable)")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    try:
        report = audit_contract(args.input, api_key=args.key)
        if args.output:
            Path(args.output).write_text(report, encoding="utf-8")
            print(f"📑 Audit report saved -> {args.output}")
        else:
            print("\n📑 Contract Audit Report:")
            print(report)
    except Exception as e:
        print(f"❌ Contract audit failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
