! intersect_AB_t.f90
! Intersection of line AB with triangle t, 3-dimensional.
! Miroslav Broz (miroslav.broz@email.cz), Oct 26th 2022

! Reference: https://www.iue.tuwien.ac.at/phd/ertl/node114.html
! Note: p = A + B*x, not (B-A)*x

module intersect_AB_t_module

contains

subroutine intersect_AB_t(A, B, t, C, has_solution)

use vector_product_module

implicit none
double precision, dimension(3), intent(in) :: A, B
double precision, dimension(3,3), intent(in) :: t
double precision, dimension(3), intent(out) :: C
logical, intent(out) :: has_solution

integer :: i
double precision, dimension(3) :: area
double precision, parameter :: EPS = 0.d0

do i = 1, 3
  C = vector_product(t(mod(i,3)+1,:)-A, t(mod(i+1,3)+1,:)-A)
  area(i) = 0.5d0*dot_product(B, C)
enddo

if ((area(1).ge.-EPS).and.(area(2).ge.-EPS).and.(area(3).ge.-EPS)) then
  has_solution = .true.
else if ((area(1).le.+EPS).and.(area(2).le.+EPS).and.(area(3).le.+EPS)) then
  has_solution = .true.
else
  has_solution = .false.
endif

if (has_solution) then
  C = (/0.d0, 0.d0, 0.d0/)
  area = area/sum(area)
  do i = 1, 3
    C = C + area(i)*t(i,:)
  enddo
endif

return
end subroutine intersect_AB_t

end module intersect_AB_t_module


