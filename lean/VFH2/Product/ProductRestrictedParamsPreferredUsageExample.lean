import VFH2.Product.ProductRestrictedParamsPreferredFrontDoor

namespace VFH2
namespace ProductRestrictedParamsPreferredUsageExample

/--
Small downstream example for the C35D validation boundary.

The caller supplies only construction data and enters the proof spine through
the preferred public API. It does not call the raw noncoverage, certificate, or
direct erase-construction front doors.
-/
noncomputable example
    (n d : Nat)
    (missing : ProductIndex d) :=
  ProductRestrictedParamsPreferredFrontDoor.currentBestMainTheorem
    n d missing

end ProductRestrictedParamsPreferredUsageExample
end VFH2
