.PHONY: exec
exec:
	@./a.out

.PHONY: init
init:
	@read -p "Directory Name: " fn; \
	mkdir "src/$$fn"; \
	cp sample/*.cpp src/$$fn;

.PHONY: copy
copy:
	find ./sample -name "*.cpp" -type f -exec cp ./src.cpp {} \;
