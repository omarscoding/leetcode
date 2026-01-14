class SegmentTree:
    def __init__(self, xs):
        self.xs = list(xs)
        self.n = len(self.xs) - 1
        self.covered_count = [0] * (4 * self.n)
        self.covered_width = [0] * (4 * self.n)
    
    def add(self, i, j, val):
        self._add(0, 0, self.n - 1, i, j, val)
    
    def get_covered_width(self):
        return self.covered_width[0]
    
    def _add(self, tree_index, lo, hi, i, j, val):
        if j <= self.xs[lo] or self.xs[hi + 1] <= i:
            return
        
        if i <= self.xs[lo] and self.xs[hi + 1] <= j:
            self.covered_count[tree_index] += val
        else:
            mid = (lo + hi) // 2
            self._add(2 * tree_index + 1, lo, mid, i, j, val)
            self._add(2 * tree_index + 2, mid + 1, hi, i, j, val)
        
        if self.covered_count[tree_index] > 0:
            self.covered_width[tree_index] = self.xs[hi + 1] - self.xs[lo]
        elif lo == hi:
            self.covered_width[tree_index] = 0
        else:
            self.covered_width[tree_index] = (
                self.covered_width[2 * tree_index + 1] + 
                self.covered_width[2 * tree_index + 2]
            )


class Solution(object):
    def separateSquares(self, squares):
        # 1. Create events and collect x-coordinates
        events = []  # (y, delta, xl, xr)
        x_coords = set()
        
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # opening
            events.append((y + l, -1, x, x + l)) # closing
            x_coords.add(x)
            x_coords.add(x + l)
        
        events.sort()
        
        # 2. Calculate total area
        total_area = self.get_total_area(events, x_coords)
        half_area = total_area / 2.0
        
        # 3. Sweep from bottom, accumulate area
        area = 0
        prev_y = 0
        seg_tree = SegmentTree(sorted(x_coords))
        
        for y, delta, xl, xr in events:
            covered_width = seg_tree.get_covered_width()
            area_gain = covered_width * (y - prev_y)
            
            # Found the line!
            if area + area_gain >= half_area:
                return prev_y + (half_area - area) / float(covered_width)
            
            area += area_gain
            seg_tree.add(xl, xr, delta)
            prev_y = y
        
        return 0.0  # Should never reach here
    
    def get_total_area(self, events, x_coords):
        """Calculate the total area of all rectangles (union)"""
        total_area = 0
        prev_y = 0
        seg_tree = SegmentTree(sorted(x_coords))
        
        for y, delta, xl, xr in events:
            total_area += seg_tree.get_covered_width() * (y - prev_y)
            seg_tree.add(xl, xr, delta)
            prev_y = y
        
        return total_area