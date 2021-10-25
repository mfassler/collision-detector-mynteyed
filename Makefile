## Build Options:
NETWORK_DISPLAY = 0
LOCAL_DISPLAY = 1

######
######   What are we building?
######

TARGET = alertIfTooClose


# Objects that must be built in order to link

OBJECTS = main.o
OBJECTS += CDNeuralNet.o

######
######   Binaries and flags
######

CPPFLAGS = -std=c++11
ifeq ($(LOCAL_DISPLAY), 1)
CPPFLAGS += -DUSE_LOCAL_DISPLAY
endif

ifeq ($(NETWORK_DISPLAY), 1)
CPPFLAGS += -DUSE_NETWORK_DISPLAY -DUSE_SCANLINE
OBJECTS += UdpSender.o
endif

CPPFLAGS += -DWITH_OPENCV 
#-DWITH_OPENCV4
CPPFLAGS += -I/usr/local/include/opencv4/
CPPFLAGS += -O3
#CPPFLAGS += -g

LD = g++

#LDFLAGS = -L/usr/local/lib/
LDFLAGS = -Wall -O3 -std=c++11     -rdynamic
LDFLAGS += -pthread
LDFLAGS += -Wl,-rpath,/home/adin/MYNT-EYE-D-SDK/3rdparty/eSPDI/linux/x64
LDLIBS += -lmynteye_depth
LDLIBS += $(shell pkg-config --libs opencv4)
#LDLIBS += -leSPDI


# Default target:
.PHONY: all
all: $(TARGET)


$(TARGET): $(OBJECTS)
	$(LD) $(LDFLAGS) $(OBJECTS) -o $@ $(LDLIBS)


.PHONY: clean
clean:
	rm -f $(OBJECTS)
	rm -f $(TARGET)


