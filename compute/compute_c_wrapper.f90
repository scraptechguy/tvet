! This automatically generated Fortran wrapper file allows codes
! written in Fortran to be called directly from C and translates all
! C-style arguments into expected Fortran-style arguments (with
! assumed size, local type declarations, etc.).


MODULE C_COMPUTE_MODULE
  IMPLICIT NONE


CONTAINS


  
  SUBROUTINE C_COMPUTE1(X_DIM_1, X_DIM_2, X, Y_DIM_1, Y_DIM_2, Y) BIND(C)
    USE COMPUTE_MODULE, ONLY: COMPUTE1
    IMPLICIT NONE
    INTEGER(KIND=SELECTED_INT_KIND(18)), INTENT(IN) :: X_DIM_1
    INTEGER(KIND=SELECTED_INT_KIND(18)), INTENT(IN) :: X_DIM_2
    REAL(KIND=KIND ( 0.0D0 )), INTENT(IN), DIMENSION(X_DIM_1,X_DIM_2) :: X
    INTEGER(KIND=SELECTED_INT_KIND(18)), INTENT(IN) :: Y_DIM_1
    INTEGER(KIND=SELECTED_INT_KIND(18)), INTENT(IN) :: Y_DIM_2
    REAL(KIND=KIND ( 0.0D0 )), INTENT(OUT), DIMENSION(Y_DIM_1,Y_DIM_2) :: Y
  
    CALL COMPUTE1(X, Y)
  END SUBROUTINE C_COMPUTE1
  
END MODULE C_COMPUTE_MODULE

