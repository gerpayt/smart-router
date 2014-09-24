#common makefile header

export BASEDIR=$(PWD)/../prj
include $(BASEDIR)/scripts/configure.mk

MODULE_EXEC	= say-stdout
MODULE_TARGET	= $(MODULE_EXEC)
LOCAL_INCLUDE	= -I$(BASEDIR)/..
LOCAL_FLAGS	= $(LOCAL_INCLUDE) $(PIC_FLAG)
LIBS	:= -L$(BASEDIR-BIN) -lmsc -ldl -lpthread -lrt

MODULE_OBJ   = \
	$(MODULE_OUTPUT)/say-stdout.o

#common makefile foot
include $(BASEDIR)/scripts/rules.mk

