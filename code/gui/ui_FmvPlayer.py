# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\ui_FmvPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlayerWindow(object):
    def setupUi(self, PlayerWindow):
        PlayerWindow.setObjectName("PlayerWindow")
        PlayerWindow.resize(742, 679)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlayerWindow.sizePolicy().hasHeightForWidth())
        PlayerWindow.setSizePolicy(sizePolicy)
        PlayerWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        PlayerWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgFMV/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlayerWindow.setWindowIcon(icon)
        PlayerWindow.setWindowOpacity(1.0)
        PlayerWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        PlayerWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(PlayerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.videoWidget = VideoWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.videoWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.videoWidget.setToolTip("")
        self.videoWidget.setStyleSheet("QWidget {\n"
" background-color:black;\n"
" } ")
        self.videoWidget.setObjectName("videoWidget")
        self.verticalLayout.addWidget(self.videoWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sliderDuration = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderDuration.sizePolicy().hasHeightForWidth())
        self.sliderDuration.setSizePolicy(sizePolicy)
        self.sliderDuration.setMinimum(0)
        self.sliderDuration.setMaximum(100)
        self.sliderDuration.setOrientation(QtCore.Qt.Horizontal)
        self.sliderDuration.setObjectName("sliderDuration")
        self.horizontalLayout_2.addWidget(self.sliderDuration)
        self.labelDuration = QtWidgets.QLabel(self.centralwidget)
        self.labelDuration.setText("")
        self.labelDuration.setObjectName("labelDuration")
        self.horizontalLayout_2.addWidget(self.labelDuration)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_Color = QtWidgets.QPushButton(self.groupBox)
        self.btn_Color.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Color.sizePolicy().hasHeightForWidth())
        self.btn_Color.setSizePolicy(sizePolicy)
        self.btn_Color.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Color.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgFMV/images/color_picker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Color.setIcon(icon1)
        self.btn_Color.setFlat(True)
        self.btn_Color.setObjectName("btn_Color")
        self.horizontalLayout_3.addWidget(self.btn_Color)
        self.btn_Rec = QtWidgets.QPushButton(self.groupBox)
        self.btn_Rec.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Rec.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgFMV/images/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/imgFMV/images/rec_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Rec.setIcon(icon2)
        self.btn_Rec.setCheckable(True)
        self.btn_Rec.setFlat(True)
        self.btn_Rec.setObjectName("btn_Rec")
        self.horizontalLayout_3.addWidget(self.btn_Rec)
        self.btn_GeoReferencing = QtWidgets.QPushButton(self.groupBox)
        self.btn_GeoReferencing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_GeoReferencing.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgFMV/images/mosaic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_GeoReferencing.setIcon(icon3)
        self.btn_GeoReferencing.setCheckable(True)
        self.btn_GeoReferencing.setFlat(True)
        self.btn_GeoReferencing.setObjectName("btn_GeoReferencing")
        self.horizontalLayout_3.addWidget(self.btn_GeoReferencing)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lb_cursor_coord = QtWidgets.QLabel(self.groupBox)
        self.lb_cursor_coord.setText("")
        self.lb_cursor_coord.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_cursor_coord.setObjectName("lb_cursor_coord")
        self.horizontalLayout_3.addWidget(self.lb_cursor_coord)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_CaptureFrame = QtWidgets.QPushButton(self.groupBox)
        self.btn_CaptureFrame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_CaptureFrame.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgFMV/images/screenshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_CaptureFrame.setIcon(icon4)
        self.btn_CaptureFrame.setFlat(True)
        self.btn_CaptureFrame.setObjectName("btn_CaptureFrame")
        self.horizontalLayout_3.addWidget(self.btn_CaptureFrame)
        self.verticalLayout.addWidget(self.groupBox)
        self.gb_PlayerControls = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_PlayerControls.sizePolicy().hasHeightForWidth())
        self.gb_PlayerControls.setSizePolicy(sizePolicy)
        self.gb_PlayerControls.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gb_PlayerControls.setStyleSheet("QGroupBox::indicator {\n"
"                 width: 13px;\n"
"                 height: 13px;\n"
"            }  \n"
"           QGroupBox::indicator:unchecked {\n"
"                 image: url(:/imgFMV/images/up.png);\n"
"            }\n"
"           QGroupBox::indicator:checked {\n"
"               image: url(:/imgFMV/images/down.png);\n"
"                }")
        self.gb_PlayerControls.setFlat(True)
        self.gb_PlayerControls.setCheckable(True)
        self.gb_PlayerControls.setObjectName("gb_PlayerControls")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gb_PlayerControls)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_previous = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_previous.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_previous.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgFMV/images/skip-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previous.setIcon(icon5)
        self.btn_previous.setFlat(True)
        self.btn_previous.setObjectName("btn_previous")
        self.horizontalLayout.addWidget(self.btn_previous)
        self.btn_rewind = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_rewind.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_rewind.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imgFMV/images/fast-rewind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rewind.setIcon(icon6)
        self.btn_rewind.setCheckable(False)
        self.btn_rewind.setFlat(True)
        self.btn_rewind.setObjectName("btn_rewind")
        self.horizontalLayout.addWidget(self.btn_rewind)
        self.btn_stop = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stop.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/imgFMV/images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon7)
        self.btn_stop.setFlat(True)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_play = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_play.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/imgFMV/images/play-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon8)
        self.btn_play.setFlat(True)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        self.btn_forward = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_forward.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_forward.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/imgFMV/images/fast-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_forward.setIcon(icon9)
        self.btn_forward.setCheckable(False)
        self.btn_forward.setAutoDefault(True)
        self.btn_forward.setFlat(True)
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout.addWidget(self.btn_forward)
        self.btn_next = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/imgFMV/images/skip-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon10)
        self.btn_next.setFlat(True)
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout.addWidget(self.btn_next)
        self.btn_repeat = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_repeat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_repeat.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/imgFMV/images/repeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_repeat.setIcon(icon11)
        self.btn_repeat.setCheckable(True)
        self.btn_repeat.setFlat(True)
        self.btn_repeat.setObjectName("btn_repeat")
        self.horizontalLayout.addWidget(self.btn_repeat)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.btn_volume = QtWidgets.QPushButton(self.gb_PlayerControls)
        self.btn_volume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_volume.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.btn_volume.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/imgFMV/images/volume_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_volume.setIcon(icon12)
        self.btn_volume.setFlat(True)
        self.btn_volume.setObjectName("btn_volume")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_volume)
        self.volumeSlider = QtWidgets.QSlider(self.gb_PlayerControls)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.volumeSlider)
        self.horizontalLayout.addLayout(self.formLayout)
        self.v_label = QtWidgets.QLabel(self.gb_PlayerControls)
        self.v_label.setStyleSheet("color: #898989")
        self.v_label.setObjectName("v_label")
        self.horizontalLayout.addWidget(self.v_label)
        self.verticalLayout.addWidget(self.gb_PlayerControls)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.progressBarProcessor = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarProcessor.sizePolicy().hasHeightForWidth())
        self.progressBarProcessor.setSizePolicy(sizePolicy)
        self.progressBarProcessor.setMinimumSize(QtCore.QSize(0, 13))
        self.progressBarProcessor.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.progressBarProcessor.setFont(font)
        self.progressBarProcessor.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 0px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #2196f3;\n"
"    width: 2px;\n"
"    margin: 0.2px;\n"
"}")
        self.progressBarProcessor.setProperty("value", 0)
        self.progressBarProcessor.setInvertedAppearance(False)
        self.progressBarProcessor.setObjectName("progressBarProcessor")
        self.horizontalLayout_4.addWidget(self.progressBarProcessor)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        PlayerWindow.setCentralWidget(self.centralwidget)
        self.menubarwidget = QtWidgets.QMenuBar(PlayerWindow)
        self.menubarwidget.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubarwidget.setStyleSheet("QMenuBar {\n"
"    background-color: transparent;\n"
"}")
        self.menubarwidget.setObjectName("menubarwidget")
        self.menuFile = QtWidgets.QMenu(self.menubarwidget)
        self.menuFile.setObjectName("menuFile")
        self.menuFrames = QtWidgets.QMenu(self.menubarwidget)
        self.menuFrames.setObjectName("menuFrames")
        self.menuMetadata = QtWidgets.QMenu(self.menubarwidget)
        self.menuMetadata.setObjectName("menuMetadata")
        self.menuConverter = QtWidgets.QMenu(self.menubarwidget)
        self.menuConverter.setObjectName("menuConverter")
        self.menuInfo = QtWidgets.QMenu(self.menubarwidget)
        self.menuInfo.setObjectName("menuInfo")
        self.menuPlot_Bitrate = QtWidgets.QMenu(self.menubarwidget)
        self.menuPlot_Bitrate.setObjectName("menuPlot_Bitrate")
        self.menuUtils = QtWidgets.QMenu(self.menubarwidget)
        self.menuUtils.setObjectName("menuUtils")
        PlayerWindow.setMenuBar(self.menubarwidget)
        self.statusbar = QtWidgets.QStatusBar(PlayerWindow)
        self.statusbar.setObjectName("statusbar")
        PlayerWindow.setStatusBar(self.statusbar)
        self.actionGray = QtWidgets.QAction(PlayerWindow)
        self.actionGray.setCheckable(True)
        self.actionGray.setObjectName("actionGray")
        self.actionEdge_Detection = QtWidgets.QAction(PlayerWindow)
        self.actionEdge_Detection.setCheckable(True)
        self.actionEdge_Detection.setObjectName("actionEdge_Detection")
        self.actionCapture_Current_Frame = QtWidgets.QAction(PlayerWindow)
        self.actionCapture_Current_Frame.setObjectName("actionCapture_Current_Frame")
        self.actionExtract_All_Frames = QtWidgets.QAction(PlayerWindow)
        self.actionExtract_All_Frames.setObjectName("actionExtract_All_Frames")
        self.actionShow_Metadata = QtWidgets.QAction(PlayerWindow)
        self.actionShow_Metadata.setObjectName("actionShow_Metadata")
        self.actionConverter_Video = QtWidgets.QAction(PlayerWindow)
        self.actionConverter_Video.setObjectName("actionConverter_Video")
        self.actionSave_Video_Info = QtWidgets.QAction(PlayerWindow)
        self.actionSave_Video_Info.setObjectName("actionSave_Video_Info")
        self.actionAudio = QtWidgets.QAction(PlayerWindow)
        self.actionAudio.setObjectName("actionAudio")
        self.actionVideo = QtWidgets.QAction(PlayerWindow)
        self.actionVideo.setObjectName("actionVideo")
        self.actionAudio_Video = QtWidgets.QAction(PlayerWindow)
        self.actionAudio_Video.setObjectName("actionAudio_Video")
        self.actionSave_Audio = QtWidgets.QAction(PlayerWindow)
        self.actionSave_Audio.setObjectName("actionSave_Audio")
        self.actionSave_Video = QtWidgets.QAction(PlayerWindow)
        self.actionSave_Video.setObjectName("actionSave_Video")
        self.actionSave_All = QtWidgets.QAction(PlayerWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionShow_Video_Info = QtWidgets.QAction(PlayerWindow)
        self.actionShow_Video_Info.setObjectName("actionShow_Video_Info")
        self.actionInvert_Color = QtWidgets.QAction(PlayerWindow)
        self.actionInvert_Color.setCheckable(True)
        self.actionInvert_Color.setObjectName("actionInvert_Color")
        self.actionMono_Filter = QtWidgets.QAction(PlayerWindow)
        self.actionMono_Filter.setCheckable(True)
        self.actionMono_Filter.setObjectName("actionMono_Filter")
        self.actionCanny_edge_detection = QtWidgets.QAction(PlayerWindow)
        self.actionCanny_edge_detection.setCheckable(True)
        self.actionCanny_edge_detection.setObjectName("actionCanny_edge_detection")
        self.actionZoom_Rectangle = QtWidgets.QAction(PlayerWindow)
        self.actionZoom_Rectangle.setCheckable(True)
        self.actionZoom_Rectangle.setEnabled(True)
        self.actionZoom_Rectangle.setObjectName("actionZoom_Rectangle")
        self.actionMagnifying_glass = QtWidgets.QAction(PlayerWindow)
        self.actionMagnifying_glass.setCheckable(True)
        self.actionMagnifying_glass.setObjectName("actionMagnifying_glass")
        self.actionAuto_Contrast_Filter = QtWidgets.QAction(PlayerWindow)
        self.actionAuto_Contrast_Filter.setCheckable(True)
        self.actionAuto_Contrast_Filter.setObjectName("actionAuto_Contrast_Filter")
        self.actionCreate_Mosaic = QtWidgets.QAction(PlayerWindow)
        self.actionCreate_Mosaic.setObjectName("actionCreate_Mosaic")
        self.actionDraw_Pinpoint = QtWidgets.QAction(PlayerWindow)
        self.actionDraw_Pinpoint.setCheckable(True)
        self.actionDraw_Pinpoint.setObjectName("actionDraw_Pinpoint")
        self.actionDraw_Line = QtWidgets.QAction(PlayerWindow)
        self.actionDraw_Line.setCheckable(True)
        self.actionDraw_Line.setObjectName("actionDraw_Line")
        self.actionDraw_Polygon = QtWidgets.QAction(PlayerWindow)
        self.actionDraw_Polygon.setCheckable(True)
        self.actionDraw_Polygon.setObjectName("actionDraw_Polygon")
        self.actionObject_Tracking = QtWidgets.QAction(PlayerWindow)
        self.actionObject_Tracking.setObjectName("actionObject_Tracking")
        self.menuFile.addAction(self.actionGray)
        self.menuFile.addAction(self.actionInvert_Color)
        self.menuFile.addAction(self.actionMono_Filter)
        self.menuFile.addAction(self.actionCanny_edge_detection)
        self.menuFile.addAction(self.actionAuto_Contrast_Filter)
        self.menuFrames.addAction(self.actionCapture_Current_Frame)
        self.menuFrames.addAction(self.actionExtract_All_Frames)
        self.menuMetadata.addAction(self.actionShow_Metadata)
        self.menuConverter.addAction(self.actionConverter_Video)
        self.menuInfo.addAction(self.actionShow_Video_Info)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.actionSave_Video_Info)
        self.menuPlot_Bitrate.addAction(self.actionAudio)
        self.menuPlot_Bitrate.addAction(self.actionVideo)
        self.menuPlot_Bitrate.addSeparator()
        self.menuPlot_Bitrate.addAction(self.actionSave_Audio)
        self.menuPlot_Bitrate.addAction(self.actionSave_Video)
        self.menuUtils.addAction(self.actionMagnifying_glass)
        self.menuUtils.addAction(self.actionDraw_Pinpoint)
        self.menuUtils.addAction(self.actionDraw_Line)
        self.menuUtils.addAction(self.actionDraw_Polygon)
        self.menuUtils.addAction(self.actionObject_Tracking)
        self.menubarwidget.addAction(self.menuFile.menuAction())
        self.menubarwidget.addAction(self.menuUtils.menuAction())
        self.menubarwidget.addAction(self.menuFrames.menuAction())
        self.menubarwidget.addAction(self.menuMetadata.menuAction())
        self.menubarwidget.addAction(self.menuConverter.menuAction())
        self.menubarwidget.addAction(self.menuInfo.menuAction())
        self.menubarwidget.addAction(self.menuPlot_Bitrate.menuAction())

        self.retranslateUi(PlayerWindow)
        self.gb_PlayerControls.toggled['bool'].connect(PlayerWindow.toggleGroup)
        self.btn_play.clicked['bool'].connect(PlayerWindow.playClicked)
        self.sliderDuration.sliderMoved['int'].connect(PlayerWindow.seek)
        self.volumeSlider.sliderMoved['int'].connect(PlayerWindow.setVolume)
        self.actionGray.triggered['bool'].connect(PlayerWindow.grayFilter)
        self.btn_CaptureFrame.clicked.connect(PlayerWindow.ExtractCurrentFrame)
        self.btn_Color.clicked.connect(PlayerWindow.showColorDialog)
        self.btn_volume.clicked.connect(PlayerWindow.setMuted)
        self.btn_stop.clicked['bool'].connect(PlayerWindow.stop)
        self.btn_previous.clicked.connect(PlayerWindow.StartMedia)
        self.btn_next.clicked.connect(PlayerWindow.EndMedia)
        self.btn_repeat.toggled['bool'].connect(PlayerWindow.AutoRepeat)
        self.actionShow_Metadata.triggered.connect(PlayerWindow.OpenQgsFmvMetadata)
        self.actionExtract_All_Frames.triggered.connect(PlayerWindow.ExtractAllFrames)
        self.actionCapture_Current_Frame.triggered.connect(PlayerWindow.ExtractCurrentFrame)
        self.actionSave_Video_Info.triggered.connect(PlayerWindow.saveInfoToJson)
        self.actionAudio_Video.triggered.connect(PlayerWindow.CreateBitratePlot)
        self.actionAudio.triggered.connect(PlayerWindow.CreateBitratePlot)
        self.actionVideo.triggered.connect(PlayerWindow.CreateBitratePlot)
        self.actionSave_All.triggered.connect(PlayerWindow.CreateBitratePlot)
        self.actionSave_Audio.triggered.connect(PlayerWindow.CreateBitratePlot)
        self.actionSave_Video.triggered.connect(PlayerWindow.CreateBitratePlot)
        self.actionShow_Video_Info.triggered.connect(PlayerWindow.showVideoInfo)
        self.actionConverter_Video.triggered.connect(PlayerWindow.convertVideo)
        self.btn_rewind.clicked.connect(PlayerWindow.rewindMedia)
        self.btn_forward.clicked.connect(PlayerWindow.forwardMedia)
        self.btn_Rec.clicked['bool'].connect(PlayerWindow.RecordVideo)
        self.actionInvert_Color.triggered['bool'].connect(PlayerWindow.invertColorFilter)
        self.actionCanny_edge_detection.triggered['bool'].connect(PlayerWindow.edgeFilter)
        self.actionMono_Filter.triggered['bool'].connect(PlayerWindow.monoFilter)
        self.actionDraw_Pinpoint.triggered['bool'].connect(PlayerWindow.pointDrawer)
        self.actionMagnifying_glass.triggered['bool'].connect(PlayerWindow.magnifier)
        self.actionAuto_Contrast_Filter.triggered['bool'].connect(PlayerWindow.autoContrastFilter)
        self.actionCreate_Mosaic.triggered['bool'].connect(PlayerWindow.createMosaic)
        self.btn_GeoReferencing.clicked['bool'].connect(PlayerWindow.createMosaic)
        self.actionDraw_Line.triggered['bool'].connect(PlayerWindow.lineDrawer)
        self.actionObject_Tracking.triggered['bool'].connect(PlayerWindow.ojectTracking)
        self.actionDraw_Polygon.triggered['bool'].connect(PlayerWindow.polygonDrawer)
        QtCore.QMetaObject.connectSlotsByName(PlayerWindow)

    def retranslateUi(self, PlayerWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayerWindow.setWindowTitle(_translate("PlayerWindow", "Player"))
        self.groupBox.setTitle(_translate("PlayerWindow", "Video Tools"))
        self.btn_Color.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Color dialog</p></body></html>"))
        self.btn_Color.setShortcut(_translate("PlayerWindow", "Ctrl+C"))
        self.btn_Rec.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Record</p></body></html>"))
        self.btn_Rec.setShortcut(_translate("PlayerWindow", "Ctrl+Shift+R"))
        self.btn_GeoReferencing.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Create Mosaic</p></body></html>"))
        self.btn_GeoReferencing.setShortcut(_translate("PlayerWindow", "Ctrl+Shift+M"))
        self.btn_CaptureFrame.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Capture current frame</p></body></html>"))
        self.btn_CaptureFrame.setShortcut(_translate("PlayerWindow", "Ctrl+Shift+Q"))
        self.gb_PlayerControls.setTitle(_translate("PlayerWindow", "Controls"))
        self.btn_previous.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Start Of Media</p></body></html>"))
        self.btn_rewind.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Rewind</p></body></html>"))
        self.btn_stop.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Stop</p></body></html>"))
        self.btn_play.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Play/Pause</p></body></html>"))
        self.btn_forward.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Forward</p></body></html>"))
        self.btn_next.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>End Of Media</p></body></html>"))
        self.btn_repeat.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Repeat</p></body></html>"))
        self.btn_volume.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Mute/Unmute</p></body></html>"))
        self.btn_volume.setShortcut(_translate("PlayerWindow", "Ctrl+Shift+U"))
        self.volumeSlider.setToolTip(_translate("PlayerWindow", "<html><head/><body><p>Volume</p></body></html>"))
        self.v_label.setText(_translate("PlayerWindow", "100%"))
        self.progressBarProcessor.setFormat(_translate("PlayerWindow", "Background Progress . . . %p%"))
        self.menuFile.setTitle(_translate("PlayerWindow", "Filters"))
        self.menuFrames.setTitle(_translate("PlayerWindow", "Frames"))
        self.menuMetadata.setTitle(_translate("PlayerWindow", "Metadata"))
        self.menuConverter.setTitle(_translate("PlayerWindow", "Converter"))
        self.menuInfo.setTitle(_translate("PlayerWindow", "Information"))
        self.menuPlot_Bitrate.setTitle(_translate("PlayerWindow", "Plot Bitrate"))
        self.menuUtils.setTitle(_translate("PlayerWindow", "Utils"))
        self.actionGray.setText(_translate("PlayerWindow", "Gray Scale"))
        self.actionEdge_Detection.setText(_translate("PlayerWindow", "Edge Detection"))
        self.actionCapture_Current_Frame.setText(_translate("PlayerWindow", "Capture Current Frame"))
        self.actionCapture_Current_Frame.setShortcut(_translate("PlayerWindow", "Ctrl+Shift+Q"))
        self.actionExtract_All_Frames.setText(_translate("PlayerWindow", "Extract All Frames"))
        self.actionExtract_All_Frames.setShortcut(_translate("PlayerWindow", "Ctrl+Shift+A"))
        self.actionShow_Metadata.setText(_translate("PlayerWindow", "Show Metadata"))
        self.actionShow_Metadata.setShortcut(_translate("PlayerWindow", "Ctrl+Shift+M"))
        self.actionConverter_Video.setText(_translate("PlayerWindow", "Converter Video"))
        self.actionSave_Video_Info.setText(_translate("PlayerWindow", "Save Video Info to Json"))
        self.actionAudio.setText(_translate("PlayerWindow", "Show Audio"))
        self.actionVideo.setText(_translate("PlayerWindow", "Show Video"))
        self.actionAudio_Video.setText(_translate("PlayerWindow", "Show All"))
        self.actionSave_Audio.setText(_translate("PlayerWindow", "Save Audio"))
        self.actionSave_Video.setText(_translate("PlayerWindow", "Save Video"))
        self.actionSave_All.setText(_translate("PlayerWindow", "Save All"))
        self.actionShow_Video_Info.setText(_translate("PlayerWindow", "Show Video Info"))
        self.actionInvert_Color.setText(_translate("PlayerWindow", "Invert Color"))
        self.actionMono_Filter.setText(_translate("PlayerWindow", "Mono Filter"))
        self.actionCanny_edge_detection.setText(_translate("PlayerWindow", "Canny edge detection"))
        self.actionZoom_Rectangle.setText(_translate("PlayerWindow", "Zoom Rectangle"))
        self.actionMagnifying_glass.setText(_translate("PlayerWindow", "Magnifying glass"))
        self.actionAuto_Contrast_Filter.setText(_translate("PlayerWindow", "Auto Contrast Filter"))
        self.actionCreate_Mosaic.setText(_translate("PlayerWindow", "Create Mosaic"))
        self.actionDraw_Pinpoint.setText(_translate("PlayerWindow", "Draw Pinpoint"))
        self.actionDraw_Line.setText(_translate("PlayerWindow", "Draw Line"))
        self.actionDraw_Polygon.setText(_translate("PlayerWindow", "Draw Polygon"))
        self.actionObject_Tracking.setText(_translate("PlayerWindow", "Object Tracking"))

from QGIS_FMV.video.QgsVideo import VideoWidget
from QGIS_FMV.gui import resources_rc
