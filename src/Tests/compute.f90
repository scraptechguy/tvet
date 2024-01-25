
module compute_module

contains

subroutine compute1(x, y)

double precision, dimension(:,:), intent(in) :: x
double precision, dimension(:,:), intent(out) :: y

y = x**2

print *, "x = ", x
print *, "y = ", y

return
end subroutine compute1

end module compute_module
