from local_communication_service import LocalCommunicationService as local_communication_service

hotword = local_communication_service.getInstance().read_hotword()
print(hotword)