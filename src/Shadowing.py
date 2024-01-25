#!/usr/bin/env python3

import numpy as np

def intersect_AB_t(A, B, t):
  """
  Intersection of line AB with triangle t, 3-dimensional.

  Reference: https://www.iue.tuwien.ac.at/phd/ertl/node114.html
  Note: p = A + B*x, not (B-A)*x

  """

  EPS = 0.0
  area = np.zeros(3)

  for i in range(3):
    C = np.cross(t[i%3,:]-A, t[(i+1)%3,:]-A)
    area[i] = 0.5*np.dot(B, C)

  if area[0] >= -EPS and area[1] >= -EPS and area[2] >= -EPS:
    has_solution = True
  elif area[0] <= +EPS and area[1] <= +EPS and area[2] <= +EPS:
    has_solution = True
  else:
    has_solution = False

  if has_solution:
    C = np.zeros(3)
    area /= np.sum(area)
    for i in range(3):
      C = C + area[i]*t[i,:]

  return C, has_solution

def non(mu_i, mu_e):
  """Non-illuminated || non-visible won't be computed."""

  nu_i = np.ones(len(mu_i))
  nu_e = np.ones(len(mu_e))

  for i in range(len(mu_i)):
    if mu_i[i] == 0.0 or mu_e[i] == 0.0:
      nu_i[i] = 0.0
      nu_e[i] = 0.0

  return nu_i, nu_e

def nu(faces, nodes, normals, centres, s, nu_i):
  """Shadowing, non-convex version."""

  t = np.zeros((3,3))

  for i in range(len(faces)):

    if nu_i[i] > 0.0:

      A = centres[i,:]
      B = s
 
      j = 0
      while j < len(faces) and nu_i[i] > 0.0:
        if i != j:
          if nu_i[j] > 0.0:
 
            C = centres[j,:] - centres[i,:]
            tmp = np.dot(C, normals[i,:])
            if tmp > 0.0:
 
              for k in range(3):
                t[k,:] = nodes[faces[j,k],:]
 
              C, has_solution = intersect_AB_t(A, B, t)
 
              if has_solution:
                nu_i[i] = 0.0
        j += 1

  return nu_i

def main():
  pass

if __name__ == "__main__":
  main()