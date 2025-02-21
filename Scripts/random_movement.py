import random
from pxr import Usd, UsdGeom

# Get the stage and the sphere's transform node
stage = Usd.Stage.Open("random_study.usd")
sphere = UsdGeom.Xform.Define(stage, "sphere")

# Set a range for random movement
min_range = -10
max_range = 10

# Create a random movement over time
for frame in range(0, 100):  # Set the range for frames
    x = random.uniform(min_range, max_range)
    y = random.uniform(min_range, max_range)
    z = random.uniform(min_range, max_range)

    # Create a new Xform for the random translation
    transform = UsdGeom.XformOp(UsdGeom.XformOp.TypeTranslate)
    transform.Set(time=frame, value=(x, y, z))
    sphere.AddXformOp(transform)

# Save the stage with the changes
stage.GetRootLayer().Save()