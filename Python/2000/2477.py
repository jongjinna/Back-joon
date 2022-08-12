n = int(input())
width_list = []
width_idx_list = []
height_list = []
height_idx_list = []

small_area = 0
large_area = 0
for i in range(6):
  a, b = map(int, input().split())
  if a == 1 or a == 2:
    width_list.append(b)
    width_idx_list.append(i)
  if a == 3 or a == 4:
    height_list.append(b)
    height_idx_list.append(i)

large_area = max(width_list) * max(height_list)
wid_idx=width_idx_list[width_list.index(max(width_list))]
hei_idx=height_idx_list[height_list.index(max(height_list))]

if wid_idx < 3:
  s_wid_idx = wid_idx+3
else:
  s_wid_idx = wid_idx-3
if hei_idx < 3:
  s_hei_idx = hei_idx+3
else:
  s_hei_idx = hei_idx-3

small_hei = height_list[height_idx_list.index(s_wid_idx)]
small_wid = width_list[width_idx_list.index(s_hei_idx)]
small_area = small_hei * small_wid

print((large_area-small_area)*n)
