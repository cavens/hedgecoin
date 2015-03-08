data campaigns[2^80](recipient, goal, deadline, contrib_total, contrib_count, contribs[2^50](sender, value))

def create_campaign(id, recipient, goal, timelimit):
    if self.campaigns[id].recipient:
        return(0)
    self.campaigns[id].recipient = recipient
    self.campaigns[id].goal = goal
    self.campaigns[id].deadline = block.timestamp + timelimit

def contribute(id):
    # Update contribution total
    total_contributed = self.campaigns[id].contrib_total + msg.value
    self.campaigns[id].contrib_total = total_contributed

    # Record new contribution
    sub_index = self.campaigns[id].contrib_count
    self.campaigns[id].contribs[sub_index].sender = msg.sender
    self.campaigns[id].contribs[sub_index].value = msg.value
    self.campaigns[id].contrib_count = sub_index + 1

    # Enough funding?
    if total_contributed >= self.campaigns[id].goal:
        send(self.campaigns[id].recipient, total_contributed)
        self.clear(id)
        return(1)

    # Expired?
    if block.timestamp > self.campaigns[id].deadline:
        i = 0
        c = self.campaigns[id].contrib_count
        while i < c:
            send(self.campaigns[id].contribs[i].sender, self.campaigns[id].contribs[i].value)
            i += 1
        self.clear(id)
        return(2)

def progress_report(id):
    return(self.campaigns[id].contrib_total)

# Clearing function for internal use
def clear(id):
    if self == msg.sender:
        self.campaigns[id].recipient = 0
        self.campaigns[id].goal = 0
        self.campaigns[id].deadline = 0
        c = self.campaigns[id].contrib_count
        self.campaigns[id].contrib_count = 0
        self.campaigns[id].contrib_total = 0
        i = 0
        while i < c:
            self.campaigns[id].contribs[i].sender = 0
            self.campaigns[id].contribs[i].value = 0
            i += 1