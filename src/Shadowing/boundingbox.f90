! bbox.f90
! Bounding boxes.
! Miroslav Broz (miroslav.broz@email.cz), Nov 3rd 2022

module boundingbox_module

contains

subroutine boundingbox(faces, nodes, s, boxes)

use vector_product_module
use normalize_module

implicit none
integer, dimension(:,:), intent(in) :: faces
double precision, dimension(:,:), intent(in) :: nodes
double precision, dimension(3), intent(in) :: s
double precision, dimension(:,:), pointer, intent(out) :: boxes

integer :: i, j, k, l
double precision, dimension(3) :: hatu, hatv, hatw
double precision :: tmp
double precision, dimension(:), pointer, save :: u, v

integer, save :: i1st = 0

if (i1st.eq.0) then
  allocate(u(size(nodes,1)))
  allocate(v(size(nodes,1)))
  allocate(boxes(size(faces,1),4))
  i1st = 1
endif

hatw = s
hatu = (/-s(2), s(1), 0.d0/)
tmp = sqrt(dot_product(hatu,hatu))
if (tmp.gt.0.d0) then
  hatu = hatu/tmp
else
  hatu = (/1.d0, 0.d0, 0.d0/)
endif
hatv = -vector_product(hatu, hatw)

!$omp parallel do private(i) shared(nodes,hatu,hatv,u,v)
do i = 1, size(nodes,1)
  u(i) = dot_product(hatu, nodes(i,:))
  v(i) = dot_product(hatv, nodes(i,:))
enddo
!$omp end parallel do

!$omp parallel do private(i,j,k,l) shared(faces,boxes,u,v)
do i = 1, size(faces,1)
  j = faces(i,1)
  k = faces(i,2)
  l = faces(i,3)
  boxes(i,1) = min(min(u(j),u(k)),u(l))
  boxes(i,2) = max(max(u(j),u(k)),u(l))
  boxes(i,3) = min(min(v(j),v(k)),v(l))
  boxes(i,4) = max(max(v(j),v(k)),v(l))
enddo
!$omp end parallel do

return
end subroutine boundingbox

end module boundingbox_module


