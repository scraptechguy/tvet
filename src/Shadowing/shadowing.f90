! shadowing.f90
! Shadowing, non-convex version.
! Miroslav Broz (miroslav.broz@email.cz), Oct 26th 2022

module shadowing_module

contains

! Dicrectional cosine.

subroutine mu(normals, s, mu_i)

implicit none
double precision, dimension(:,:), intent(in) :: normals
double precision, dimension(3), intent(in) :: s
double precision, dimension(:), intent(out) :: mu_i

integer :: i

!$omp parallel do private(i) shared(normals,mu_i,s)
do i = 1, size(normals,1)
  mu_i(i) = max(dot_product(normals(i,:), s), 0.d0)
enddo
!$omp end parallel do

return
end subroutine mu

! Non-illuminated || non-visible won't be computed.

subroutine non(mu_i, mu_e, nu_i, nu_e)

implicit none
double precision, dimension(:), intent(in) :: mu_i, mu_e
double precision, dimension(:), intent(out) :: nu_i, nu_e

integer :: i

nu_i = 1.d0
nu_e = 1.d0
!$omp parallel do private(i) shared(mu_i,mu_e,nu_i,nu_e)
do i = 1, size(mu_i,1)
  if ((mu_i(i).eq.0.d0).or.(mu_e(i).eq.0.d0)) then
    nu_i(i) = 0.d0
    nu_e(i) = 0.d0
  endif
enddo
!$omp end parallel do

return
end subroutine non

! Mutual shadowing.

subroutine nu(faces, nodes, normals, centres, s, nu_i)

use boundingbox_module
use intersect_AB_t_module

implicit none
integer, dimension(:,:), intent(in) :: faces
double precision, dimension(:,:), intent(in) :: nodes, normals, centres
double precision, dimension(3), intent(in) :: s
double precision, dimension(:), intent(inout) :: nu_i

integer :: i, j, k
double precision, dimension(3,3) :: t
double precision, dimension(3) :: A, B, C
double precision, dimension(3) :: area
double precision :: tmp
logical :: has_solution

double precision, dimension(:,:), pointer, save :: boxes

call boundingbox(faces, nodes, s, boxes)

!$omp parallel do private(i,j,k,A,B,C,t,has_solution,tmp,area) shared(nodes,faces,centres,s,nu_i)
do i = 1, size(faces,1)
  if (nu_i(i).gt.0.d0) then

    A = centres(i,:)
    B = s

    j = 1
    do while ((j.le.size(faces,1)).and.(nu_i(i).gt.0.d0))

      if (i.ne.j) then
        if (nu_i(j).gt.0.d0) then

          if ((boxes(j,2).lt.boxes(i,1)).or.(boxes(j,1).gt.boxes(i,2) &
            .or.(boxes(j,4).lt.boxes(i,3)).or.(boxes(j,3).gt.boxes(i,4)))) then
            j = j+1
            cycle
          endif

          C = centres(j,:)-centres(i,:)
          tmp = dot_product(C, normals(i,:))
          if (tmp.gt.0.d0) then

            do k = 1, 3
              t(k,:) = nodes(faces(j,k),:)
            enddo

            call intersect_AB_t(A, B, t, C, has_solution)

            if (has_solution) then
              nu_i(i) = 0.d0
            endif

          endif

        endif
      endif

      j = j+1
    enddo  ! j

  endif
enddo ! i
!$omp end parallel do

return
end subroutine nu

end module shadowing_module


