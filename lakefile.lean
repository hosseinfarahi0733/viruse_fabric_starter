import Lake
open Lake DSL

package «viruse_fabric_starter» where
  -- Restricted VF-H2 Lean scaffold only.
  -- This package does not claim a full formal proof.

lean_lib VFH2 where
  roots := #[`VFH2.RestrictedBridge.Scaffold]
