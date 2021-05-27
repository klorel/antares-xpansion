# ===========================================================================
# CMake configuration
# ===========================================================================

# ===========================================================================
# Targets
# ===========================================================================

# ---------------------------------------------------------------------------
# Sequential Benders Exe
# ---------------------------------------------------------------------------

add_executable (lp_debugger 
	${CMAKE_CURRENT_SOURCE_DIR}/main.cpp
)

target_link_libraries (lp_debugger 
	PRIVATE 
		${PROJECT_NAME}::benders_sequential_core
		logger_lib)

install(TARGETS lp_debugger DESTINATION bin)
