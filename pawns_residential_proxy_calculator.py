#!/usr/bin/env python3
"""
Pawns.app Referral Bonus & Residential Proxy Bandwidth Calculator 2026.
"""
import argparse

TIER_RATES = [
    (100, 1.50),
    (50, 2.00),
    (10, 2.50),
    (0, 3.00)
]

def calculate(volume_gb, referral_bonus):
    rate = 3.00
    for threshold, price in TIER_RATES:
        if volume_gb >= threshold:
            rate = price
            break

    gross_cost = volume_gb * rate
    bonus_credit = 3.00 if referral_bonus else 0.00
    net_cost = max(0.0, gross_cost - bonus_credit)

    print("=" * 60)
    print("Pawns.app Residential Proxy & Referral Calculator")
    print("=" * 60)
    print(f"Data Volume Purchased:   {volume_gb} GB (Never Expiring)")
    print(f"Volume Bandwidth Rate:   ${rate:.2f}/GB")
    print(f"Gross Purchase Price:    ${gross_cost:.2f}")
    if referral_bonus:
        print(f"Referral Code Bonus:     -${bonus_credit:.2f} (Applied)")
    print(f"Final Net Payment:       ${net_cost:.2f}")
    print("=" * 60)
    return net_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pawns.app Pricing Calculator")
    parser.add_argument("--volume-gb", type=int, default=20)
    parser.add_argument("--referral-bonus", action="store_true", default=True)
    args = parser.parse_args()
    calculate(args.volume_gb, args.referral_bonus)
