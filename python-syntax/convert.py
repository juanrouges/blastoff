def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    # Example: (30°C x 1.8) + 32 = 86°F
    # Example: (50°F - 32) x .5556 = 10°C
    if unit_in == "c":
      return (temp * 1.8) + 32
    elif unit_in == "f" : 
      return (temp - 32) * 0.5556
    else:
      return f"Invalid unit entered {unit_in}"


# print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
# print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
# print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
# print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

