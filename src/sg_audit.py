"""
sg_audit.py (skeleton)

Purpose:
- Detect overly permissive AWS Security Group inbound rules
  e.g., 0.0.0.0/0 open ports, wide port ranges.

Safety:
- Week1: Read-only audit (no modifications).
- Default scope (planned): limit by tag Project=aws-infra-blueprint.
"""

def main() -> int:
    print("sg_audit.py is not implemented yet (Week1 skeleton).")
    print("Planned: list security groups, scan inbound rules, report risky patterns.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
