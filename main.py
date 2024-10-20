
def count_batteries_by_health(present_capacities):
   rated_capacity = 120  # rated capacity in Ah
   counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
   }

   for present_capacity in present_capacities:
        # Calculate SoH
        soh = (100 * present_capacity) / rated_capacity
        
        # Classification based on SoH
        if soh > 80:
            counts["healthy"] += 1
        elif 62 < soh <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

   return counts



def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()




