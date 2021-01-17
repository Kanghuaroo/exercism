-- Table to be returned by the hello-world module.
local hello_world = {}

-- Add the hello() function to the table returned by this module.
function hello_world.hello()
  -- Write some code here to pass the test suite.

  return 'Hello, World!'
end

-- Return the hello_world table to make it accessible as a module.
return hello_world
