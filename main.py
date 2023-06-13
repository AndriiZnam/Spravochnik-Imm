try:
  print("Hello world")
except Exception as e:
  logging.error("An error occurred: %s", type(e).__name__)
  logging.exception("Error details:") 
