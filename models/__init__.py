from models.lm_models.ShowAttendTell import ShowAttendTellModel
from models.lm_models.HRNN import ShowAttendTellModel as HRNN
from models.lm_models.CMG_HRNN import ShowAttendTellModel as CMG_HRNN
from models.event_encoder import Basic_Encoder, TSRM_Encoder

def setup_caption_model(opt):
    if opt.caption_decoder_type == 'show_attend_tell':
        model = ShowAttendTellModel(opt)
    elif opt.caption_decoder_type == 'hrnn':
        model = HRNN(opt)
    elif opt.caption_decoder_type == 'cmg_hrnn':
        model = CMG_HRNN(opt)
    else:
        raise AssertionError('args error: caption_model')
    return model

def setup_event_encoder(opt):
    if opt.event_encoder_type == 'basic':
        model = Basic_Encoder(opt)
    elif opt.event_encoder_type == 'tsrm':
        model = TSRM_Encoder(opt)
    else:
        raise AssertionError('args error: event_encoder_type')
    return model