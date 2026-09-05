const MUSIC_DATA = {
  "semitonesPerOctave": 12,
  "lowFretWrapLimit": 2,
  "upperShapeOffsetThreshold": 5,
  "highPositionOffsetThreshold": 7,
  "highPositionWrapLimit": 5,
  "cagedFretSearchOctaves": 3,
  "chromaticScale": [
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
    "A",
    "A#",
    "B"
  ],
  "stringTuningOffsets": {
    "1": 4,
    "2": 11,
    "3": 7,
    "4": 2,
    "5": 9,
    "6": 4
  },
  "stringNames": {
    "1": "E",
    "2": "B",
    "3": "G",
    "4": "D",
    "5": "A",
    "6": "E"
  },
  "cagedInversion": "Standard Shape",
  "chordQualities": {
    "Major 7 (R-3-5-7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7,
        "7": 11
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5",
        "7": "7"
      },
      "voicingNote": "Standard four-note Drop 2/Drop 3 seventh-chord voicing."
    },
    "Minor 7 (R-b3-5-b7)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 7,
        "7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "5",
        "7": "b7"
      },
      "voicingNote": "Standard four-note Drop 2/Drop 3 minor seventh voicing."
    },
    "Dominant 7 (R-3-5-b7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7,
        "7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5",
        "7": "b7"
      },
      "voicingNote": "Standard four-note Drop 2/Drop 3 dominant seventh voicing."
    },
    "Major 6 (R-3-5-6)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7,
        "7": 9
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5",
        "7": "6"
      },
      "voicingNote": "Uses the current seventh-chord slot as a sixth."
    },
    "Minor 6 (R-b3-5-6)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 7,
        "7": 9
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "5",
        "7": "6"
      },
      "voicingNote": "Uses the current seventh-chord slot as a sixth."
    },
    "Minor 7 b5 (R-b3-b5-b7)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 6,
        "7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "b5",
        "7": "b7"
      },
      "voicingNote": "Common four-note half-diminished guitar voicing."
    },
    "Diminished 7 (R-b3-b5-bb7)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 6,
        "7": 9
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "b5",
        "7": "bb7"
      },
      "voicingNote": "Compact symmetrical four-note diminished seventh voicing."
    },
    "Minor Major 7 (R-b3-5-7)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 7,
        "7": 11
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "5",
        "7": "7"
      },
      "voicingNote": "Four-note voicing, but some grips may feel less common."
    },
    "Augmented Major 7 (R-3-#5-7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 8,
        "7": 11
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "#5",
        "7": "7"
      },
      "voicingNote": "Four-note augmented major seventh voicing."
    },
    "Augmented Dominant 7 (R-3-#5-b7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 8,
        "7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "#5",
        "7": "b7"
      },
      "voicingNote": "Four-note augmented dominant voicing."
    },
    "Dominant 7 b5 (R-3-b5-b7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 6,
        "7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "b5",
        "7": "b7"
      },
      "voicingNote": "Common four-note altered dominant voicing."
    },
    "Dominant 7 #5 (R-3-#5-b7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 8,
        "7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "#5",
        "7": "b7"
      },
      "voicingNote": "Common four-note altered dominant voicing."
    },
    "Dominant 7 sus4 (R-4-5-b7)": {
      "intervals": {
        "R": 0,
        "3": 5,
        "5": 7,
        "7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "4",
        "5": "5",
        "7": "b7"
      },
      "voicingNote": "Four-note suspended dominant voicing."
    },
    "Major 7 #11 shell (R-3-7-#11)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 11,
        "7": 6
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "7",
        "7": "#11"
      },
      "voicingNote": "Shell voicing: omits the fifth to fit a four-note guitar grip."
    },
    "Dominant 9 shell (R-3-b7-9)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 10,
        "7": 14
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "b7",
        "7": "9"
      },
      "voicingNote": "Shell voicing: omits the fifth to fit a four-note guitar grip."
    },
    "Minor 9 shell (R-b3-b7-9)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 10,
        "7": 14
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "b7",
        "7": "9"
      },
      "voicingNote": "Shell voicing: omits the fifth to fit a four-note guitar grip."
    },
    "Major 9 shell (R-3-7-9)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 11,
        "7": 14
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "7",
        "7": "9"
      },
      "voicingNote": "Shell voicing: omits the fifth to fit a four-note guitar grip."
    },
    "6/9 shell (R-3-6-9)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 9,
        "7": 14
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "6",
        "7": "9"
      },
      "voicingNote": "Shell voicing: four-note sixth/ninth guitar voicing."
    },
    "Minor 6/9 shell (R-b3-6-9)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 9,
        "7": 14
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "6",
        "7": "9"
      },
      "voicingNote": "Shell voicing: four-note minor sixth/ninth guitar voicing."
    },
    "9sus4 shell (R-4-b7-9)": {
      "intervals": {
        "R": 0,
        "3": 5,
        "5": 10,
        "7": 14
      },
      "displayLabels": {
        "R": "R",
        "3": "4",
        "5": "b7",
        "7": "9"
      },
      "voicingNote": "Shell voicing: suspended dominant sound with the fifth omitted."
    },
    "13 shell (R-3-b7-13)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 10,
        "7": 21
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "b7",
        "7": "13"
      },
      "voicingNote": "Shell voicing: omits the fifth and ninth/eleventh color tones."
    },
    "Minor 11 shell (R-b3-b7-11)": {
      "intervals": {
        "R": 0,
        "3": 3,
        "5": 10,
        "7": 17
      },
      "displayLabels": {
        "R": "R",
        "3": "b3",
        "5": "b7",
        "7": "11"
      },
      "voicingNote": "Shell voicing: omits the fifth and ninth to fit a four-note guitar grip."
    }
  },
  "cagedChordQualities": {
    "Major triad (R-3-5)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5"
      },
      "voicingNote": "Standard movable CAGED major-triad shape."
    },
    "Minor triad (R-b3-5)": {
      "intervals": {
        "R": 0,
        "b3": 3,
        "5": 7
      },
      "displayLabels": {
        "R": "R",
        "b3": "b3",
        "5": "5"
      },
      "voicingNote": "Minor-triad variation based on the movable CAGED shape."
    },
    "Dominant 7 (R-3-5-b7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7,
        "b7": 10
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5",
        "b7": "b7"
      },
      "voicingNote": "Movable CAGED dominant seventh shape."
    },
    "Major 7 (R-3-5-7)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7,
        "7": 11
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5",
        "7": "7"
      },
      "voicingNote": "Movable CAGED major seventh shape."
    },
    "Minor 7 (R-b3-5-b7)": {
      "intervals": {
        "R": 0,
        "b3": 3,
        "5": 7,
        "b7": 10
      },
      "displayLabels": {
        "R": "R",
        "b3": "b3",
        "5": "5",
        "b7": "b7"
      },
      "voicingNote": "Movable CAGED minor seventh shape."
    },
    "Major 6 (R-3-5-6)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7,
        "6": 9
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5",
        "6": "6"
      },
      "voicingNote": "Movable CAGED sixth-chord shape."
    },
    "Minor 6 (R-b3-5-6)": {
      "intervals": {
        "R": 0,
        "b3": 3,
        "5": 7,
        "6": 9
      },
      "displayLabels": {
        "R": "R",
        "b3": "b3",
        "5": "5",
        "6": "6"
      },
      "voicingNote": "Movable CAGED minor sixth-chord shape."
    },
    "Suspended 2 (R-2-5)": {
      "intervals": {
        "R": 0,
        "2": 2,
        "5": 7
      },
      "displayLabels": {
        "R": "R",
        "2": "2",
        "5": "5"
      },
      "voicingNote": "Movable CAGED suspended second shape."
    },
    "Suspended 4 (R-4-5)": {
      "intervals": {
        "R": 0,
        "4": 5,
        "5": 7
      },
      "displayLabels": {
        "R": "R",
        "4": "4",
        "5": "5"
      },
      "voicingNote": "Movable CAGED suspended fourth shape."
    },
    "Add 9 (R-3-5-9)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "5": 7,
        "9": 14
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "5": "5",
        "9": "9"
      },
      "voicingNote": "Movable CAGED add9 shape."
    },
    "Diminished triad (R-b3-b5)": {
      "intervals": {
        "R": 0,
        "b3": 3,
        "b5": 6
      },
      "displayLabels": {
        "R": "R",
        "b3": "b3",
        "b5": "b5"
      },
      "voicingNote": "Movable CAGED diminished-triad shape."
    },
    "Augmented triad (R-3-#5)": {
      "intervals": {
        "R": 0,
        "3": 4,
        "#5": 8
      },
      "displayLabels": {
        "R": "R",
        "3": "3",
        "#5": "#5"
      },
      "voicingNote": "Movable CAGED augmented-triad shape."
    }
  },
  "baseShapes": {
    "Drop 2": {
      "Root Position": {
        "4": [
          0,
          "R"
        ],
        "3": [
          0,
          "5"
        ],
        "2": [
          1,
          "7"
        ],
        "1": [
          0,
          "3"
        ]
      },
      "1st Inversion": {
        "4": [
          4,
          "3"
        ],
        "3": [
          3,
          "7"
        ],
        "2": [
          3,
          "R"
        ],
        "1": [
          3,
          "5"
        ]
      },
      "2nd Inversion": {
        "4": [
          7,
          "5"
        ],
        "3": [
          7,
          "R"
        ],
        "2": [
          8,
          "3"
        ],
        "1": [
          7,
          "7"
        ]
      },
      "3rd Inversion": {
        "4": [
          11,
          "7"
        ],
        "3": [
          11,
          "3"
        ],
        "2": [
          10,
          "5"
        ],
        "1": [
          10,
          "R"
        ]
      }
    },
    "Drop 3": {
      "Root Position": {
        "5": [
          0,
          "R"
        ],
        "3": [
          1,
          "7"
        ],
        "2": [
          1,
          "3"
        ],
        "1": [
          0,
          "5"
        ]
      },
      "1st Inversion": {
        "5": [
          4,
          "3"
        ],
        "3": [
          3,
          "R"
        ],
        "2": [
          3,
          "5"
        ],
        "1": [
          4,
          "7"
        ]
      },
      "2nd Inversion": {
        "5": [
          7,
          "5"
        ],
        "3": [
          8,
          "3"
        ],
        "2": [
          7,
          "7"
        ],
        "1": [
          7,
          "R"
        ]
      },
      "3rd Inversion": {
        "5": [
          11,
          "7"
        ],
        "3": [
          10,
          "5"
        ],
        "2": [
          10,
          "R"
        ],
        "1": [
          11,
          "3"
        ]
      }
    }
  },
  "cagedShapes": {
    "CAGED C Shape": {
      "root_note": "C",
      "layouts": {
        "Major triad (R-3-5)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            2,
            "3"
          ],
          "3": [
            0,
            "5"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            0,
            "3"
          ]
        },
        "Minor triad (R-b3-5)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            1,
            "b3"
          ],
          "3": [
            0,
            "5"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            3,
            "5"
          ]
        },
        "Dominant 7 (R-3-5-b7)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            2,
            "3"
          ],
          "3": [
            3,
            "b7"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            0,
            "3"
          ]
        },
        "Major 7 (R-3-5-7)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            2,
            "3"
          ],
          "3": [
            0,
            "5"
          ],
          "2": [
            0,
            "7"
          ],
          "1": [
            0,
            "3"
          ]
        },
        "Minor 7 (R-b3-5-b7)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            1,
            "b3"
          ],
          "3": [
            3,
            "b7"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            3,
            "5"
          ]
        },
        "Major 6 (R-3-5-6)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            2,
            "3"
          ],
          "3": [
            2,
            "6"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            0,
            "3"
          ]
        },
        "Minor 6 (R-b3-5-6)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            1,
            "b3"
          ],
          "3": [
            2,
            "6"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            3,
            "5"
          ]
        },
        "Suspended 2 (R-2-5)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            0,
            "2"
          ],
          "3": [
            0,
            "5"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            3,
            "5"
          ]
        },
        "Suspended 4 (R-4-5)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            3,
            "4"
          ],
          "3": [
            0,
            "5"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            1,
            "4"
          ]
        },
        "Add 9 (R-3-5-9)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            2,
            "3"
          ],
          "3": [
            0,
            "5"
          ],
          "2": [
            3,
            "9"
          ],
          "1": [
            0,
            "3"
          ]
        },
        "Diminished triad (R-b3-b5)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            1,
            "b3"
          ],
          "3": [
            2,
            "b5"
          ],
          "2": [
            1,
            "R"
          ]
        },
        "Augmented triad (R-3-#5)": {
          "5": [
            3,
            "R"
          ],
          "4": [
            2,
            "3"
          ],
          "3": [
            1,
            "#5"
          ],
          "2": [
            1,
            "R"
          ],
          "1": [
            0,
            "3"
          ]
        }
      }
    },
    "CAGED A Shape": {
      "root_note": "A",
      "layouts": {
        "Major triad (R-3-5)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            2,
            "3"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Minor triad (R-b3-5)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            1,
            "b3"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Dominant 7 (R-3-5-b7)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            0,
            "b7"
          ],
          "2": [
            2,
            "3"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Major 7 (R-3-5-7)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            1,
            "7"
          ],
          "2": [
            2,
            "3"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Minor 7 (R-b3-5-b7)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            0,
            "b7"
          ],
          "2": [
            1,
            "b3"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Major 6 (R-3-5-6)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            2,
            "3"
          ],
          "1": [
            2,
            "6"
          ]
        },
        "Minor 6 (R-b3-5-6)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            1,
            "b3"
          ],
          "1": [
            2,
            "6"
          ]
        },
        "Suspended 2 (R-2-5)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            0,
            "2"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Suspended 4 (R-4-5)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            3,
            "4"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Add 9 (R-3-5-9)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            2,
            "5"
          ],
          "3": [
            4,
            "9"
          ],
          "2": [
            2,
            "3"
          ],
          "1": [
            0,
            "5"
          ]
        },
        "Diminished triad (R-b3-b5)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            1,
            "b5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            1,
            "b3"
          ]
        },
        "Augmented triad (R-3-#5)": {
          "5": [
            0,
            "R"
          ],
          "4": [
            3,
            "#5"
          ],
          "3": [
            2,
            "R"
          ],
          "2": [
            2,
            "3"
          ],
          "1": [
            1,
            "#5"
          ]
        }
      }
    },
    "CAGED G Shape": {
      "root_note": "G",
      "layouts": {
        "Major triad (R-3-5)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            2,
            "3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            0,
            "3"
          ],
          "1": [
            3,
            "R"
          ]
        },
        "Minor triad (R-b3-5)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            1,
            "b3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            3,
            "b3"
          ],
          "1": [
            3,
            "R"
          ]
        },
        "Dominant 7 (R-3-5-b7)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            2,
            "3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            0,
            "3"
          ],
          "1": [
            1,
            "b7"
          ]
        },
        "Major 7 (R-3-5-7)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            2,
            "3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            0,
            "3"
          ],
          "1": [
            2,
            "7"
          ]
        },
        "Minor 7 (R-b3-5-b7)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            1,
            "b3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            3,
            "b3"
          ],
          "1": [
            1,
            "b7"
          ]
        },
        "Major 6 (R-3-5-6)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            2,
            "3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            0,
            "3"
          ],
          "1": [
            0,
            "6"
          ]
        },
        "Minor 6 (R-b3-5-6)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            1,
            "b3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            3,
            "b3"
          ],
          "1": [
            0,
            "6"
          ]
        },
        "Suspended 2 (R-2-5)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            0,
            "2"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            3,
            "2"
          ],
          "1": [
            3,
            "R"
          ]
        },
        "Suspended 4 (R-4-5)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            3,
            "4"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            1,
            "4"
          ],
          "1": [
            3,
            "R"
          ]
        },
        "Add 9 (R-3-5-9)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            2,
            "3"
          ],
          "4": [
            0,
            "5"
          ],
          "3": [
            2,
            "9"
          ],
          "2": [
            0,
            "3"
          ],
          "1": [
            3,
            "R"
          ]
        },
        "Diminished triad (R-b3-b5)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            1,
            "b3"
          ],
          "4": [
            2,
            "b5"
          ],
          "3": [
            0,
            "R"
          ]
        },
        "Augmented triad (R-3-#5)": {
          "6": [
            3,
            "R"
          ],
          "5": [
            2,
            "3"
          ],
          "4": [
            1,
            "#5"
          ],
          "3": [
            0,
            "R"
          ],
          "2": [
            0,
            "3"
          ],
          "1": [
            3,
            "R"
          ]
        }
      }
    },
    "CAGED E Shape": {
      "root_note": "E",
      "layouts": {
        "Major triad (R-3-5)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            2,
            "R"
          ],
          "3": [
            1,
            "3"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Minor triad (R-b3-5)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            2,
            "R"
          ],
          "3": [
            0,
            "b3"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Dominant 7 (R-3-5-b7)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            0,
            "b7"
          ],
          "3": [
            1,
            "3"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Major 7 (R-3-5-7)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            1,
            "7"
          ],
          "3": [
            1,
            "3"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Minor 7 (R-b3-5-b7)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            0,
            "b7"
          ],
          "3": [
            0,
            "b3"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Major 6 (R-3-5-6)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            2,
            "R"
          ],
          "3": [
            1,
            "3"
          ],
          "2": [
            2,
            "6"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Minor 6 (R-b3-5-6)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            2,
            "R"
          ],
          "3": [
            0,
            "b3"
          ],
          "2": [
            2,
            "6"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Suspended 2 (R-2-5)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            4,
            "2"
          ],
          "3": [
            4,
            "5"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Suspended 4 (R-4-5)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            2,
            "R"
          ],
          "3": [
            2,
            "4"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Add 9 (R-3-5-9)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            2,
            "5"
          ],
          "4": [
            4,
            "9"
          ],
          "3": [
            1,
            "3"
          ],
          "2": [
            0,
            "5"
          ],
          "1": [
            0,
            "R"
          ]
        },
        "Diminished triad (R-b3-b5)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            1,
            "b5"
          ],
          "4": [
            2,
            "R"
          ],
          "3": [
            0,
            "b3"
          ]
        },
        "Augmented triad (R-3-#5)": {
          "6": [
            0,
            "R"
          ],
          "5": [
            3,
            "#5"
          ],
          "4": [
            2,
            "R"
          ],
          "3": [
            1,
            "3"
          ],
          "2": [
            1,
            "#5"
          ],
          "1": [
            0,
            "R"
          ]
        }
      }
    },
    "CAGED D Shape": {
      "root_note": "D",
      "layouts": {
        "Major triad (R-3-5)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            3,
            "R"
          ],
          "1": [
            2,
            "3"
          ]
        },
        "Minor triad (R-b3-5)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            3,
            "R"
          ],
          "1": [
            1,
            "b3"
          ]
        },
        "Dominant 7 (R-3-5-b7)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            1,
            "b7"
          ],
          "1": [
            2,
            "3"
          ]
        },
        "Major 7 (R-3-5-7)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            2,
            "7"
          ],
          "1": [
            2,
            "3"
          ]
        },
        "Minor 7 (R-b3-5-b7)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            1,
            "b7"
          ],
          "1": [
            1,
            "b3"
          ]
        },
        "Major 6 (R-3-5-6)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            0,
            "6"
          ],
          "1": [
            2,
            "3"
          ]
        },
        "Minor 6 (R-b3-5-6)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            0,
            "6"
          ],
          "1": [
            1,
            "b3"
          ]
        },
        "Suspended 2 (R-2-5)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            3,
            "R"
          ],
          "1": [
            0,
            "2"
          ]
        },
        "Suspended 4 (R-4-5)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            3,
            "R"
          ],
          "1": [
            3,
            "4"
          ]
        },
        "Add 9 (R-3-5-9)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            2,
            "5"
          ],
          "2": [
            3,
            "R"
          ],
          "1": [
            0,
            "9"
          ]
        },
        "Diminished triad (R-b3-b5)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            1,
            "b5"
          ],
          "2": [
            3,
            "R"
          ],
          "1": [
            1,
            "b3"
          ]
        },
        "Augmented triad (R-3-#5)": {
          "4": [
            0,
            "R"
          ],
          "3": [
            3,
            "#5"
          ],
          "2": [
            3,
            "R"
          ],
          "1": [
            2,
            "3"
          ]
        }
      }
    }
  },
  "maxNotesInDropModel": 4,
  "maxNotesInCagedModel": 6,
  "easyMaxFretSpan": 3,
  "stretchyMaxFretSpan": 5,
  "maxRecommendedFret": 18,
  "openFret": 0,
  "gridMinFret": 0,
  "minVisibleFretSpan": 4,
  "fretPaddingBefore": 1,
  "fretPaddingAfter": 2
};

const SELECTORS = {
  rootNote: document.querySelector("#rootNote"),
  chordFamily: document.querySelector("#chordFamily"),
  chordType: document.querySelector("#chordType"),
  inversion: document.querySelector("#inversion"),
  fretboard: document.querySelector("#fretboard"),
  title: document.querySelector("#title"),
  formula: document.querySelector("#formula"),
  status: document.querySelector("#status"),
  playability: document.querySelector("#playability"),
  voicingNote: document.querySelector("#voicingNote"),
};

const VIEW = Object.freeze({ width: 1120, height: 480, left: 92, right: 32, top: 54, bottom: 72 });
const FIRST_STRING = 1;
const LAST_STRING = 6;
const STRING_GAP_COUNT = LAST_STRING - FIRST_STRING;

function isCagedShape(chordType) {
  return Object.prototype.hasOwnProperty.call(MUSIC_DATA.cagedShapes, chordType);
}

function getChordTypes() {
  return [...Object.keys(MUSIC_DATA.baseShapes), ...Object.keys(MUSIC_DATA.cagedShapes)];
}

function getChordFamilies(chordType) {
  return Object.keys(isCagedShape(chordType) ? MUSIC_DATA.cagedChordQualities : MUSIC_DATA.chordQualities);
}

function getInversions(chordType) {
  if (isCagedShape(chordType)) {
    return [MUSIC_DATA.cagedInversion];
  }
  return Object.keys(MUSIC_DATA.baseShapes[chordType]);
}

function chordQuality(chordType, chordFamily) {
  if (isCagedShape(chordType) && MUSIC_DATA.cagedChordQualities[chordFamily]) {
    return MUSIC_DATA.cagedChordQualities[chordFamily];
  }
  if (MUSIC_DATA.chordQualities[chordFamily]) {
    return MUSIC_DATA.chordQualities[chordFamily];
  }
  return MUSIC_DATA.cagedChordQualities[chordFamily];
}

function populateSelect(select, values, selectedValue) {
  select.replaceChildren();
  values.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    select.appendChild(option);
  });
  select.value = values.includes(selectedValue) ? selectedValue : values[0];
}

function refreshDependentControls() {
  const chordType = SELECTORS.chordType.value;
  populateSelect(SELECTORS.chordFamily, getChordFamilies(chordType), SELECTORS.chordFamily.value);
  populateSelect(SELECTORS.inversion, getInversions(chordType), SELECTORS.inversion.value);
}

function calculateVoicing(chordType, inversion, chordFamily, rootNote) {
  return isCagedShape(chordType)
    ? calculateCagedVoicing(chordType, inversion, chordFamily, rootNote)
    : calculateDropVoicing(chordType, inversion, chordFamily, rootNote);
}

function calculateDropVoicing(chordType, inversion, chordFamily, rootNote) {
  const rootIndex = MUSIC_DATA.chromaticScale.indexOf(rootNote);
  const baseLayout = MUSIC_DATA.baseShapes[chordType][inversion];
  const quality = chordQuality(chordType, chordFamily);
  const positions = Object.entries(baseLayout).map(([string, note]) => {
    const stringNumber = Number(string);
    const [baseFretOffset, intervalType] = note;
    const intervalModifier = quality.intervals[intervalType];
    const targetPitch = positiveModulo(rootIndex + intervalModifier, MUSIC_DATA.semitonesPerOctave);
    const stringOpenPitch = MUSIC_DATA.stringTuningOffsets[string];
    let fret = positiveModulo(targetPitch - stringOpenPitch, MUSIC_DATA.semitonesPerOctave);

    if (fret < MUSIC_DATA.lowFretWrapLimit && baseFretOffset > MUSIC_DATA.upperShapeOffsetThreshold) {
      fret += MUSIC_DATA.semitonesPerOctave;
    } else if (baseFretOffset >= MUSIC_DATA.highPositionOffsetThreshold && fret < MUSIC_DATA.highPositionWrapLimit) {
      fret += MUSIC_DATA.semitonesPerOctave;
    }

    return { string: stringNumber, fret, label: quality.displayLabels[intervalType] };
  });

  return { chordType, inversion, chordFamily, rootNote, positions, voicingNote: quality.voicingNote, maxNoteCount: null };
}

function calculateCagedVoicing(chordType, inversion, chordFamily, rootNote) {
  const rootIndex = MUSIC_DATA.chromaticScale.indexOf(rootNote);
  const shape = MUSIC_DATA.cagedShapes[chordType];
  const shapeRootIndex = MUSIC_DATA.chromaticScale.indexOf(shape.root_note);
  const shapeOffset = positiveModulo(rootIndex - shapeRootIndex, MUSIC_DATA.semitonesPerOctave);
  const quality = chordQuality(chordType, chordFamily);
  const layout = shape.layouts[chordFamily];
  const positions = Object.entries(layout).map(([string, note]) => {
    const stringNumber = Number(string);
    const [baseFret, intervalType] = note;
    const intervalModifier = quality.intervals[intervalType];
    const targetPitch = positiveModulo(rootIndex + intervalModifier, MUSIC_DATA.semitonesPerOctave);
    const preferredFret = baseFret + shapeOffset;
    return {
      string: stringNumber,
      fret: nearestFretForPitch(string, targetPitch, preferredFret),
      label: quality.displayLabels[intervalType],
    };
  });

  return {
    chordType,
    inversion,
    chordFamily,
    rootNote,
    positions,
    voicingNote: quality.voicingNote,
    maxNoteCount: MUSIC_DATA.maxNotesInCagedModel,
  };
}

function nearestFretForPitch(string, targetPitch, preferredFret) {
  const baseFret = positiveModulo(targetPitch - MUSIC_DATA.stringTuningOffsets[string], MUSIC_DATA.semitonesPerOctave);
  const candidates = Array.from(
    { length: MUSIC_DATA.cagedFretSearchOctaves },
    (_, octave) => baseFret + MUSIC_DATA.semitonesPerOctave * octave
  );
  return candidates.reduce((best, candidate) => (
    Math.abs(candidate - preferredFret) < Math.abs(best - preferredFret) ? candidate : best
  ));
}

function assessPlayability(voicing) {
  const frets = voicing.positions.map((position) => position.fret);
  const frettedPositions = frets.filter((fret) => fret > MUSIC_DATA.openFret);
  const fretSpan = frettedPositions.length ? Math.max(...frettedPositions) - Math.min(...frettedPositions) : 0;
  const maxNoteCount = voicing.maxNoteCount ?? MUSIC_DATA.maxNotesInDropModel;

  if (frets.length > maxNoteCount) {
    return { rating: "not recommended", fretSpan, message: `Not recommended: this voicing uses more than ${maxNoteCount} sounded strings.` };
  }

  if (frettedPositions.length && Math.max(...frettedPositions) > MUSIC_DATA.maxRecommendedFret) {
    return {
      rating: "not recommended",
      fretSpan,
      message: `Not recommended: highest fret is above ${MUSIC_DATA.maxRecommendedFret}. ${voicing.voicingNote}`,
    };
  }

  if (fretSpan <= MUSIC_DATA.easyMaxFretSpan) {
    return { rating: "playable", fretSpan, message: `Playable: fret span ${fretSpan}. ${voicing.voicingNote}` };
  }

  if (fretSpan <= MUSIC_DATA.stretchyMaxFretSpan) {
    return { rating: "stretchy", fretSpan, message: `Stretchy: fret span ${fretSpan}. ${voicing.voicingNote}` };
  }

  return { rating: "not recommended", fretSpan, message: `Not recommended: fret span ${fretSpan}. ${voicing.voicingNote}` };
}

function fretGridBounds(frets) {
  return [
    Math.max(MUSIC_DATA.gridMinFret, Math.min(...frets) - MUSIC_DATA.fretPaddingBefore),
    Math.max(MUSIC_DATA.minVisibleFretSpan, Math.max(...frets) + MUSIC_DATA.fretPaddingAfter),
  ];
}

function positiveModulo(value, divisor) {
  return ((value % divisor) + divisor) % divisor;
}

function svgEl(tag, attrs = {}) {
  const element = document.createElementNS("http://www.w3.org/2000/svg", tag);
  Object.entries(attrs).forEach(([key, value]) => element.setAttribute(key, value));
  return element;
}

function markerColor(label) {
  return label === "R" ? "var(--root)" : "var(--tone)";
}

function drawFretboard(voicing) {
  const frets = voicing.positions.map((position) => position.fret);
  const [minFret, maxFret] = fretGridBounds(frets);
  const boardWidth = VIEW.width - VIEW.left - VIEW.right;
  const boardHeight = VIEW.height - VIEW.top - VIEW.bottom;
  const fretCount = maxFret - minFret;
  const fretWidth = boardWidth / fretCount;
  const stringGap = boardHeight / STRING_GAP_COUNT;

  SELECTORS.fretboard.replaceChildren();
  SELECTORS.fretboard.setAttribute("viewBox", `0 0 ${VIEW.width} ${VIEW.height}`);

  SELECTORS.fretboard.appendChild(svgEl("rect", {
    x: 0,
    y: 0,
    width: VIEW.width,
    height: VIEW.height,
    fill: "#111111",
  }));

  for (let string = FIRST_STRING; string <= LAST_STRING; string += 1) {
    const y = VIEW.top + (string - FIRST_STRING) * stringGap;
    const lineWidth = 1 + (6 - string) * 0.45;
    SELECTORS.fretboard.appendChild(svgEl("line", {
      x1: VIEW.left,
      y1: y,
      x2: VIEW.width - VIEW.right,
      y2: y,
      stroke: "#9a9a9a",
      "stroke-width": lineWidth,
    }));
    const stringLabel = svgEl("text", {
      x: VIEW.left - 18,
      y: y + 6,
      fill: "#dddddd",
      "font-size": 18,
      "font-weight": 650,
      "text-anchor": "end",
    });
    stringLabel.textContent = `${MUSIC_DATA.stringNames[string]} (${string})`;
    SELECTORS.fretboard.appendChild(stringLabel);
  }

  for (let fret = minFret; fret <= maxFret; fret += 1) {
    const x = VIEW.left + (fret - minFret) * fretWidth;
    SELECTORS.fretboard.appendChild(svgEl("line", {
      x1: x,
      y1: VIEW.top,
      x2: x,
      y2: VIEW.top + boardHeight,
      stroke: fret === 0 ? "#f4f4f4" : "#555555",
      "stroke-width": fret === 0 ? 6 : 2,
    }));
    const fretLabel = svgEl("text", {
      x: x + 4,
      y: VIEW.height - 24,
      fill: "#dddddd",
      "font-size": 18,
      "font-weight": 650,
      "text-anchor": "start",
    });
    fretLabel.textContent = fret;
    SELECTORS.fretboard.appendChild(fretLabel);
  }

  voicing.positions.forEach((position) => {
    const fretX = VIEW.left + (position.fret - minFret) * fretWidth;
    const x = position.fret === 0 ? fretX + fretWidth * 0.5 : fretX - fretWidth * 0.5;
    const y = VIEW.top + (position.string - FIRST_STRING) * stringGap;
    SELECTORS.fretboard.appendChild(svgEl("circle", {
      cx: x,
      cy: y,
      r: 22,
      fill: markerColor(position.label),
      stroke: "#ffffff",
      "stroke-width": 3,
    }));
    const text = svgEl("text", {
      x,
      y: y + 6,
      fill: "#ffffff",
      "font-size": 16,
      "font-weight": 800,
      "text-anchor": "middle",
    });
    text.textContent = position.label;
    SELECTORS.fretboard.appendChild(text);
  });
}

function updateView() {
  refreshDependentControls();
  const voicing = calculateVoicing(
    SELECTORS.chordType.value,
    SELECTORS.inversion.value,
    SELECTORS.chordFamily.value,
    SELECTORS.rootNote.value
  );
  const playability = assessPlayability(voicing);
  const quality = chordQuality(voicing.chordType, voicing.chordFamily);

  SELECTORS.title.textContent = `${voicing.rootNote} ${voicing.chordFamily}`;
  SELECTORS.formula.textContent = Object.values(quality.displayLabels).join("-");
  SELECTORS.status.textContent = `Showing ${voicing.rootNote} ${voicing.chordFamily} as ${voicing.chordType} (${voicing.inversion}).`;
  SELECTORS.playability.textContent = playability.message;
  SELECTORS.playability.dataset.rating = playability.rating;
  SELECTORS.voicingNote.textContent = voicing.voicingNote;
  drawFretboard(voicing);
}

function init() {
  populateSelect(SELECTORS.rootNote, MUSIC_DATA.chromaticScale, "C");
  populateSelect(SELECTORS.chordType, getChordTypes(), "Drop 2");
  refreshDependentControls();

  [SELECTORS.rootNote, SELECTORS.chordFamily, SELECTORS.chordType, SELECTORS.inversion].forEach((select) => {
    select.addEventListener("change", updateView);
  });
  updateView();
}

init();
