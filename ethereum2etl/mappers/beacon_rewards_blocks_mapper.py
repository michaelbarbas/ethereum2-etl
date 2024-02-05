# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ethereum2etl.utils.string_utils import to_int
from ethereum2etl.domain.beacon_rewards_block import BeaconRewardsBlocks


class BeaconRewardsBlocksMapper(object):
    @staticmethod
    def json_dict_to_beacon_rewards_blocks(json_dict, epoch, slot):
        beacon_rewards_blocks = BeaconRewardsBlocks()

        message = json_dict.get('data', EMPTY_OBJECT)
        beacon_rewards_blocks.proposer_index = to_int(message.get('proposer_index'))
        beacon_rewards_blocks.total = message.get('total')
        beacon_rewards_blocks.attestations = message.get('attestations')
        beacon_rewards_blocks.sync_aggregate = message.get('sync_aggregate')
        beacon_rewards_blocks.proposer_slashings = message.get('proposer_slashings')
        beacon_rewards_blocks.attester_slashings = message.get('attester_slashings')
        beacon_rewards_blocks.block_epoch = epoch
        beacon_rewards_blocks.slot = slot

        return beacon_rewards_blocks

    @staticmethod
    def create_skipped_beacon_rewards_blocks(epoch, slot):
        beacon_rewards_blocks = BeaconRewardsBlocks()

        beacon_rewards_blocks.block_epoch = epoch
        beacon_rewards_blocks.slot = slot

        beacon_rewards_blocks.skipped = True

        return beacon_rewards_blocks

    @staticmethod
    def beacon_rewards_blocks_to_dict(beacon_rewards_blocks: BeaconRewardsBlocks):
        return {
            **{
                'item_type': 'beacon_rewards_blocks',
            },
            **vars(beacon_rewards_blocks),
        }


EMPTY_OBJECT = {}
EMPTY_LIST = []
