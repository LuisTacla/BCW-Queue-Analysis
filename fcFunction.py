import matplotlib.pyplot as plt

def custom_color_map(value, p5, p90, p95):
  if value > p95:
    return 'black'
  else:
    norm_value = (value - p5) / (p95 - p5)
    return plt.cm.RdYlGn_r(norm_value)
  
  